import sys
from collections import Counter, defaultdict
from random import getrandbits

input = sys.stdin.buffer.readline

output = ""
RD = getrandbits(32)

for _ in range(int(input())):
    n, k = map(int, input().split())
    a = map(int, input().split())
    b = map(int, input().split())

    counts1 = Counter(min(x % k, k - x % k) ^ RD for x in a)
    counts2 = Counter(min(x % k, k - x % k) ^ RD for x in b)
    counts = counts1 - counts2

    output += "YES\n" if all(c == 0 for c in counts.values()) else "NO\n"
print(output)
