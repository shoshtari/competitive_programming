#! /usr/bin/env python3
"""Track per-problem attempts (time taken, result, failure reason) in data.db.

Usage:
  scripts/attempts.py sync [--handle mortezamalekey]   # pull from Codeforces API
  scripts/attempts.py list [--failed]                  # print the table
  scripts/attempts.py set 2131D --time 35 --result AC --reason "off by one"

`sync` only fills empty fields, so values you set by hand are never overwritten.
"""
import argparse
import json
import sqlite3
import urllib.request
from collections import defaultdict
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "data.db"
DEFAULT_HANDLE = "mortezamalekey"
PRACTICE_TIME = 2147483647  # CF uses INT_MAX for relativeTimeSeconds in practice
SHORT = {
    "WRONG_ANSWER": "WA",
    "TIME_LIMIT_EXCEEDED": "TLE",
    "MEMORY_LIMIT_EXCEEDED": "MLE",
    "RUNTIME_ERROR": "RE",
    "COMPILATION_ERROR": "CE",
    "IDLENESS_LIMIT_EXCEEDED": "ILE",
}


def connect():
    conn = sqlite3.connect(DB_PATH)
    conn.execute(
        """
    CREATE TABLE IF NOT EXISTS attempts(
        question_id INT PRIMARY KEY,
        mode TEXT,              -- contest / virtual / practice
        result TEXT,            -- AC / FAILED
        time_taken_min INT,     -- minutes; auto-filled only for contest/virtual
        wrong_submissions INT,
        verdicts TEXT,          -- e.g. "WA x2, TLE x1"
        failure_reason TEXT,    -- your own notes
        description TEXT,       -- free notes: idea, approach, takeaways
        solved_at TEXT,
        FOREIGN KEY(question_id) REFERENCES questions(id)
    )""",
    )
    cols = [r[1] for r in conn.execute("PRAGMA table_info(attempts)")]
    if "description" not in cols:
        conn.execute("ALTER TABLE attempts ADD COLUMN description TEXT")
    return conn


def question_id(cur, pid, name=None, rating=None, url=None, tags=()):
    cur.execute(
        """INSERT INTO questions(provider, id_in_provider, name, url, rating)
           VALUES('codeforces', ?, ?, ?, ?)
           ON CONFLICT(provider, id_in_provider) DO UPDATE SET
             name = COALESCE(questions.name, excluded.name),
             url = COALESCE(questions.url, excluded.url),
             rating = COALESCE(excluded.rating, questions.rating)""",
        (pid, name, url, rating),
    )
    qid = cur.execute(
        "SELECT id FROM questions WHERE provider='codeforces' AND id_in_provider=?",
        (pid,),
    ).fetchone()[0]
    for t in tags:
        cur.execute("INSERT OR IGNORE INTO questions_tags VALUES(?, ?)", (qid, t))
    return qid


def sync(handle):
    url = f"https://codeforces.com/api/user.status?handle={handle}"
    data = json.load(urllib.request.urlopen(url, timeout=30))
    if data["status"] != "OK":
        raise SystemExit(data)

    by_problem = defaultdict(list)
    for s in data["result"]:
        p = s["problem"]
        if "contestId" not in p or s.get("verdict") in (None, "TESTING", "SKIPPED"):
            continue
        by_problem[(p["contestId"], p["index"])].append(s)

    conn = connect()
    cur = conn.cursor()
    for (cid, idx), subs in by_problem.items():
        subs.sort(key=lambda s: s["creationTimeSeconds"])
        p = subs[0]["problem"]
        url = f"https://codeforces.com/problemset/problem/{cid}/{idx}"
        qid = question_id(
            cur,
            f"{cid}{idx}",
            p.get("name"),
            p.get("rating"),
            url,
            p.get("tags", []),
        )

        ac = next((s for s in subs if s["verdict"] == "OK"), None)
        before = subs[: subs.index(ac)] if ac else subs
        counts = defaultdict(int)
        for s in before:
            counts[SHORT.get(s["verdict"], s["verdict"])] += 1
        verdicts = ", ".join(f"{k} x{v}" for k, v in counts.items()) or None

        first = ac or subs[0]
        ptype = first["author"]["participantType"]
        mode = {
            "CONTESTANT": "contest",
            "VIRTUAL": "virtual",
            "OUT_OF_COMPETITION": "contest",
        }.get(ptype, "practice")
        time_min = None
        if ac and ac["relativeTimeSeconds"] != PRACTICE_TIME and mode != "practice":
            time_min = ac["relativeTimeSeconds"] // 60
        solved_at = None
        if ac:
            solved_at = conn.execute(
                "SELECT datetime(?, 'unixepoch', 'localtime')",
                (ac["creationTimeSeconds"],),
            ).fetchone()[0]

        cur.execute("INSERT OR IGNORE INTO attempts(question_id) VALUES(?)", (qid,))
        # auto fields refresh; manual-ish fields only fill if empty
        cur.execute(
            """UPDATE attempts SET
                 mode = COALESCE(mode, ?),
                 result = ?,
                 wrong_submissions = ?,
                 verdicts = ?,
                 solved_at = ?,
                 time_taken_min = COALESCE(time_taken_min, ?)
               WHERE question_id = ?""",
            (
                mode,
                "AC" if ac else "FAILED",
                len(before),
                verdicts,
                solved_at,
                time_min,
                qid,
            ),
        )
    conn.commit()
    print(f"synced {len(by_problem)} problems from {len(data['result'])} submissions")


def set_row(args):
    conn = connect()
    cur = conn.cursor()
    qid = question_id(cur, args.problem)
    cur.execute("INSERT OR IGNORE INTO attempts(question_id) VALUES(?)", (qid,))
    fields = {
        "time_taken_min": args.time,
        "result": args.result,
        "failure_reason": args.reason,
        "description": args.description,
        "mode": args.mode,
    }
    for col, val in fields.items():
        if val is not None:
            cur.execute(
                f"UPDATE attempts SET {col} = ? WHERE question_id = ?",
                (val, qid),
            )
    conn.commit()
    show(conn, f"q.id = {qid}")


def ask(files):
    """Prompt for time/result/reason of each problem file (used by pre-commit).

    Pre-commit doesn't give hooks a stdin, so we talk to /dev/tty directly.
    With no terminal (CI, GUI git clients) it silently does nothing.
    """
    try:
        tty_in = open("/dev/tty")
        tty_out = open("/dev/tty", "w")
    except OSError:
        return

    def prompt(label, current, cast=str, choices=None):
        hint = f" [{current}]" if current not in (None, "") else ""
        opts = f" ({'/'.join(choices)})" if choices else ""
        while True:
            tty_out.write(f"  {label}{opts}{hint}: ")
            tty_out.flush()
            val = tty_in.readline().strip()
            if not val:
                return current
            if val == "-":
                return None
            if choices and val.upper() not in choices:
                continue
            try:
                return cast(val.upper() if choices else val)
            except ValueError:
                continue

    pids = []
    for f in files:
        p = Path(f)
        if p.parent.name == "codeforces" and p.suffix in (
            ".py",
            ".cpp",
            ".c",
            ".go",
            ".java",
            ".rs",
        ):
            stem = p.stem.removeprefix("incomplete_")
            if stem not in pids:
                pids.append(stem)
    if not pids:
        return

    conn = connect()
    cur = conn.cursor()
    tty_out.write("Attempt info (Enter keeps current value, '-' clears it)\n")
    for pid in pids:
        qid = question_id(cur, pid)
        cur.execute("INSERT OR IGNORE INTO attempts(question_id) VALUES(?)", (qid,))
        mode, result, time, reason, verdicts, desc = cur.execute(
            "SELECT mode, result, time_taken_min, failure_reason, verdicts, description FROM attempts WHERE question_id=?",
            (qid,),
        ).fetchone()
        tty_out.write(
            f"\n{pid}" + (f"  (CF verdicts: {verdicts})" if verdicts else "") + "\n",
        )
        mode = prompt(
            "mode",
            mode or "practice",
            choices=["CONTEST", "VIRTUAL", "PRACTICE"],
        )
        result = prompt("result", result or "AC", choices=["AC", "FAILED", "UPSOLVED"])
        time = prompt("time taken (min)", time, cast=int)
        if result != "AC" or verdicts or reason:
            reason = prompt("reason for failure", reason)
        desc = prompt("description", desc)
        cur.execute(
            "UPDATE attempts SET mode=?, result=?, time_taken_min=?, failure_reason=?, description=? WHERE question_id=?",
            (mode.lower() if mode else None, result, time, reason, desc, qid),
        )
        conn.commit()


def show(conn, where="1"):
    rows = conn.execute(
        f"""SELECT q.id_in_provider, q.rating, a.mode, a.result, a.time_taken_min,
                   a.verdicts, a.failure_reason, a.description
            FROM attempts a JOIN questions q ON q.id = a.question_id
            WHERE {where} ORDER BY a.solved_at IS NULL, a.solved_at DESC""",
    ).fetchall()
    head = (
        "problem",
        "rating",
        "mode",
        "result",
        "min",
        "verdicts",
        "reason",
        "description",
    )
    print("\t".join(head))
    for r in rows:
        print("\t".join("" if v is None else str(v) for v in r))


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("sync")
    s.add_argument("--handle", default=DEFAULT_HANDLE)
    l = sub.add_parser("list")
    l.add_argument(
        "--failed",
        action="store_true",
        help="only problems with failed submissions",
    )
    e = sub.add_parser("set")
    e.add_argument("problem", help="e.g. 2131D")
    e.add_argument("--time", type=int, help="minutes taken")
    e.add_argument("--result", choices=["AC", "FAILED", "UPSOLVED"])
    e.add_argument("--reason", help="reason for failure")
    e.add_argument("--description", help="free notes: idea, approach, takeaways")
    e.add_argument("--mode", choices=["contest", "virtual", "practice"])
    a = sub.add_parser("ask", help="interactively fill info for given problems/files")
    a.add_argument(
        "files",
        nargs="*",
        help="solution files or problem ids, e.g. codeforces/2131D.cpp or 2131D",
    )
    a.add_argument("--sync", action="store_true", help="pull Codeforces verdicts first")
    a.add_argument(
        "--last-commit",
        action="store_true",
        help="ask about solution files changed in HEAD (used by post-commit hook)",
    )
    args = ap.parse_args()

    if args.cmd == "ask":
        files = list(args.files)
        if args.last_commit:
            import subprocess

            out = subprocess.run(
                [
                    "git",
                    "diff-tree",
                    "--no-commit-id",
                    "--name-only",
                    "-r",
                    "--diff-filter=AM",
                    "HEAD",
                ],
                capture_output=True,
                text=True,
            ).stdout
            files += [f for f in out.split() if f.startswith("codeforces/")]
        if not files:
            return
        if args.sync:
            try:
                sync(DEFAULT_HANDLE)
            except Exception as ex:  # offline etc. shouldn't block commits
                print(f"sync skipped: {ex}")
        ask([f if "/" in f else f"codeforces/{f}.cpp" for f in files])
    elif args.cmd == "sync":
        sync(args.handle)
    elif args.cmd == "set":
        set_row(args)
    else:
        show(
            connect(),
            "a.wrong_submissions > 0 OR a.result != 'AC'" if args.failed else "1",
        )


if __name__ == "__main__":
    main()
