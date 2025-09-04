from typing import List


def base3(n) -> List[int]:
    res = []
    while n:
        res.append(n % 3)
        n //= 3
    return res


def solve():
    n, k = map(int, input().split())
    ans = 0
    o = base3(n)
    k -= sum(o)
    if k < 0:
        print(-1)
        return
    ind = len(o) - 1
    while k >= 3:
        while ind > 0 and o[ind] == 0:
            ind -= 1
        if ind <= 0:
            break
        while k >= 3 and o[ind] > 0:
            o[ind] -= 1
            k -= 3
            o[ind - 1] += 3

    ans = 0
    for i in range(len(o)):
        ans += int(o[i] * ((3 ** (i + 1)) + i * (3 ** (i - 1))))
    print(o, ans)


for _ in range(int(input())):
    solve()
