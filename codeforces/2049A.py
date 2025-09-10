for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    l = 0
    while l < n and a[l] == 0:
        l += 1
    r = n - 1
    while r >= 0 and a[r] == 0:
        r -= 1
    a = a[l : r + 1]
    if not a:
        print(0)
        continue

    if 0 not in a:
        print(1)
        continue
    print(2)
