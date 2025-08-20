def op():
    n = int(input())
    a = list(map(int, input().split()))
    ans = "LL"
    lasts = [a[0], a[1]]
    l = 2
    r = n - 1
    while l <= r:
        if l == r:
            ans += "R"
            break

        if lasts[0] < lasts[1]:  # we should go with decreasing

            if a[l] < a[r]:
                ans += "RL"
                lasts = [a[r], a[l]]
            else:
                ans += "LR"
                lasts = [a[l], a[r]]

            l += 1
            r -= 1

        else:  # we should go with increasing
            if a[l] > a[r]:
                ans += "RL"
                lasts = [a[r], a[l]]
            else:
                ans += "LR"
                lasts = [a[l], a[r]]

            l += 1
            r -= 1
    print(ans)


for _ in range(int(input())):
    op()
