def solve():
    n, x, y = map(int, input().split())
    ans = [-1] * n
    x -= 1
    y -= 1
    ans[x] = 0
    ans[(x + n + 1) % n] = 1
    ans[(x + n - 1) % n] = 1
    for i in range(2, n):
        right = ans[(x + n + i + 1) % n]
        left = ans[(x + n + i - 1) % n]
        options = set([0, 1, 2, 3])
        options.discard(right)
        options.discard(left)
        if (x + n + i) % n == y:
            options.discard(0)

        ans[(x + n + i) % n] = min(options)
    for i in ans:
        print(i, end=" ")
    print()


for _ in range(int(input())):
    solve()
