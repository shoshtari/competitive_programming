class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return

        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1


def op():
    n = int(input())
    a = []
    maxa = 0
    for _ in range(n):
        u, v = map(int, input().split())
        if u > v:
            u, v = v, u
        a.append((u, v))
        maxa = max(maxa, v)
        maxa = max(maxa, u)
    dsu = DSU(maxa + 1)
    ignores = set()
    for i in range(n):
        u, v = a[i]
        if dsu.find(u) == dsu.find(v):
            ignores.add(i)
        else:
            dsu.union(u, v)
    print(n - len(ignores))
    for i in range(n):
        if i in ignores:
            continue
        print(i + 1, end=" ")
    print()


for _ in range(int(input())):
    op()
