def op():
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    ans = 1
    for i in range(n):
        ans += max(a[i] - b[i], 0)
    print(ans)
    return


for _ in range(int(input())):
    op()
