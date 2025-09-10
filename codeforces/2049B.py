def solve():
    n = int(input())
    a = input()
    ans = []
    last = 0
    length = 0

    leftest_p = a.find("p")
    rightest_s = a.rfind("s")
    if "p" not in a or "s" not in a:
        print("YES")
        return

    if leftest_p < rightest_s:
        print("NO")
        return
    if leftest_p != n - 1 and rightest_s != 0:
        print("NO")
        return
    print("YES")


for _ in range(int(input())):
    solve()
