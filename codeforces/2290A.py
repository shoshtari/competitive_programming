def solve():
    a, b, c = map(int, input().split())
    a = [a, b, c]
    a.sort()
    a[0] += 1
    a[-1] -= 1
    if a[0] == a[1] and a[1] == a[2]:
        print("YES")
    else:
        print("NO")


for _ in range(int(input())):
    solve()
