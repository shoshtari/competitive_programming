from collections import Counter


def solve():
    # print("###############################")
    n = int(input())
    a = []
    for i in range(n):
        a.append(list(input()))
    visited = set()
    ans = 0
    for i in range(n):
        for j in range(n):
            repls = [(i, j), (j, n - i - 1), (n - i - 1, n - j - 1), (n - j - 1, i)]
            # print(repls)
            skip = False
            for r in repls:
                if r in visited:
                    skip = True
            if skip:
                continue
            visited.add((i, j))
            count = 0
            for r in repls:
                if a[r[0]][r[1]] == "0":
                    count += 1
            count = min(count, 4 - count)
            # print(count)
            ans += count
    print(ans)


for _ in range(int(input())):
    solve()
