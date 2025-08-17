def op():
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    if a[-1] != b[-1]:
        print("NO")
        return
    for i in range(n - 2, -1, -1):
        if a[i] == b[i]:
            continue

        for alter in (a[i + 1], b[i + 1]):
            if a[i] ^ alter == b[i]:
                break
        else:
            print("NO")
            return
    print("YES")


for _ in range(int(input())):
    op()
