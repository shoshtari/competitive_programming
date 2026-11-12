from collections import Counter


def solvek(counts: Counter, s: int):
    done = set()
    ans = 0
    for c in counts:
        done.add(c)
        rem = s - c
        if rem in done:
            continue
        ans += min(counts[c], counts[rem])
    if s % 2 == 0:
        ans += counts[s // 2] // 2

    return ans


def solve():
    n = int(input())
    a = [int(i) for i in input().split()]
    candids = set()
    for i in range(n):
        for j in range(i + 1, n):
            candids.add(a[i] + a[j])

    counts = Counter(a)
    ans = 0
    for c in candids:
        o = solvek(counts, c)
        if o > ans:
            ans = o
    print(ans)


for _ in range(int(input())):
    solve()
