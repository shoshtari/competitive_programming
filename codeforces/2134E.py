import sys

DEBUG = False


def pprint(*args, **kwargs):
    print(*args, **kwargs)
    sys.stdout.flush()


def log(*args, **kwargs):
    if DEBUG:
        pprint(*args, **kwargs)


def solve2(ans, dp, swaps):
    # solve last two
    n = len(ans) - 1

    pprint(f"throw {n - 1}")
    a = 3 - int(input())
    swaps.append(n - 1)
    pprint(f"swap {n - 1}")
    pprint(f"throw {n - 1}")
    b = 3 - int(input())
    ans[-1] = a
    ans[-2] = b
    dp[-1] = 1
    dp[-2] = 1 if ans[-2] == 2 else 2


def fill_dp(dp, ans, ind):
    log("fill dp", ind)
    dp[ind] = 1 + dp[ind + ans[ind]]


def solve3(ans, dp, swaps):
    # solve last three
    solve2(ans, dp, swaps)
    n = len(ans) - 1
    swaps.append(n - 2)
    pprint(f"swap {n - 2}")  # n - 2 and n - 1
    pprint(f"throw {n - 1}")
    a = 3 - int(input())
    ans[-3] = ans[-2]
    ans[-2] = a
    dp[-2] = 1 if ans[-2] == 2 else 2
    fill_dp(dp, ans, n - 2)


def solve():
    n = int(input())
    ans = [-1] * (n + 1)
    dp = [-1] * (n + 1)
    swaps = []

    if n % 2 == 0:
        solve2(ans, dp, swaps)
        last = n - 1
    else:
        solve3(ans, dp, swaps)
        last = n - 2
    log("DP", dp)
    log("ANS", ans)

    while last > 1:

        if dp[last] == dp[last + 1]:
            log("equal dp")
            pprint(f"throw {last - 2}")
            a = int(input())
            if a == 1 + dp[last]:
                a = 2
            else:
                a = 1

            pprint(f"swap {last - 2}")
            swaps.append(last - 2)
            pprint(f"throw {last - 2}")

            b = int(input())
            if b == 1 + dp[last]:
                b = 2
            else:
                b = 1

            ans[last - 2] = b
            ans[last - 1] = a
        else:
            log("different dp")
            pprint(f"throw {last - 1}")
            a = int(input())
            if a == 1 + dp[last]:
                a = 1
            else:
                a = 2
            pprint(f"swap {last - 2}")
            swaps.append(last - 2)
            pprint(f"throw {last - 1}")
            b = int(input())
            if b == 1 + dp[last]:
                b = 1
            else:
                b = 2
            ans[last - 2] = a
            ans[last - 1] = b
        fill_dp(dp, ans, last - 1)
        fill_dp(dp, ans, last - 2)
        last -= 2
        log("DP", dp)
        log("ANS", ans)

    log(ans)
    log(dp)
    for s in reversed(swaps):
        ans[s], ans[s + 1] = ans[s + 1], ans[s]
    ans[0] = "!"
    ans = [str(i) for i in ans]
    pprint(" ".join(ans))


for _ in range(int(input())):
    solve()
