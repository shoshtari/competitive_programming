from typing import List

def base3(n) -> List[int]:
    res = []
    while n:
        res.append(n % 3)
        n //= 3
    return res

def solve():
    n = int(input())
    ans = 0
    o = base3(n)
    for i in range(len(o)):
        ans += int(o[i] * ((3 ** (i + 1)) + i * (3 ** (i - 1))))
    print(ans)


for _ in range(int(input())):
    solve()
