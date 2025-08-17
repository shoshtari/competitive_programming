def op():
    n = int(input())
    for i in range(n):
        if i % 2:
            if i == n - 1:
                print(2, end=" ")
            else:
                print(3, end=" ")
        else:
            print(-1, end=" ")
    print()


for _ in range(int(input())):
    op()
