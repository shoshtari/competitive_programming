#! /usr/bin/env python3
import os
import sqlite3
import sys
from pathlib import Path

import pycodeforces
from rich.progress import track

# --- config ---
DB_PATH = "data.db"
CODE_DIR = "codeforces"

# file extension → language mapping
LANG_MAP = {
    ".py": "python",
    ".cpp": "cpp",
    ".c": "c",
    ".java": "java",
    ".go": "go",
    ".rs": "rust",
}


codforces_problems = None


def get_codeforces_stats(qid):

    global codforces_problems
    if codforces_problems is None:
        tmp = pycodeforces.SyncMethod().get_problemset_problems()[0].problems
        codforces_problems = {}

        for problem in tmp:
            problem_id = f"{problem.contestId}{problem.index}"
            codforces_problems[problem_id] = {
                "name": problem.name,
                "rating": problem.rating,
                "url": f"https://codeforces.com/problemset/problem/{problem.contestId}/{problem.index}",
            }
    return codforces_problems.get(qid, {"name": None, "rating": None, "url": None})


def handle_file(file: Path, cur: sqlite3.Cursor):

    stem, ext = file.stem, file.suffix
    if ext not in LANG_MAP:
        return

    lang = LANG_MAP[ext]
    qid = stem  # e.g. "2131D"
    provider = "codeforces"
    stats = get_codeforces_stats(qid)
    if not stats:
        raise ValueError(f"Question {qid} not found in Codeforces problems.")
    name = stats["name"]
    url = stats["url"]
    rating = stats["rating"]

    # insert or ignore into questions
    cur.execute(
        """
            INSERT INTO questions(provider, id_in_provider, name, url, rating)
            VALUES(?, ?, ?, ?, ?)
            ON CONFLICT(provider, id_in_provider) DO UPDATE SET rating = excluded.rating
        """,
        (provider, qid, name, url, rating),
    )

    # get the question_id
    cur.execute(
        "SELECT id FROM questions WHERE provider = ? AND id_in_provider = ?",
        (provider, qid),
    )
    question_id = cur.fetchone()[0]

    # insert or ignore into solutions
    cur.execute(
        """
            INSERT INTO solutions(question_id, language)
            SELECT ?, ?
            WHERE NOT EXISTS (
                SELECT 1 FROM solutions WHERE question_id = ? AND language = ?
            )
        """,
        (question_id, lang, question_id, lang),
    )


def main():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("CREATE INDEX IF NOT EXISTS rating_index ON questions(rating)")

    # scan directory
    for file in track(
        list(Path(CODE_DIR).iterdir()),
        description="Syncing Codeforces problems...",
    ):
        if not file.is_file():
            continue
        handle_file(file, cur)
    conn.commit()
    conn.close()
    print("✅ Sync complete.")


def main(files):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute(
        """
    CREATE TABLE IF NOT EXISTS questions(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        provider TEXT,
        id_in_provider TEXT,
        name TEXT,
        url TEXT,
        rating INT,
        UNIQUE(provider, id_in_provider)
    )""",
    )

    cur.execute(
        """
    CREATE TABLE IF NOT EXISTS solutions(
        question_id INT,
        language TEXT,
        FOREIGN KEY(question_id) REFERENCES questions(id)
    )""",
    )

    for f in track(files, description="Syncing Codeforces problems..."):
        handle_file(Path(f), cur)

    conn.commit()
    conn.close()


if __name__ == "__main__":
    # pre-commit passes changed files as arguments
    if len(sys.argv) == 1:
        # if no files are passed, sync the entire directory
        main(list(Path(CODE_DIR).iterdir()))
    else:
        files = sys.argv[1:]
        if files:
            main(files)
