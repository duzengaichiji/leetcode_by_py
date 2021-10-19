class UF:
    def __init__(self, count):
        self.count = count
        self.parent = [i for i in range(count)]

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        if rootP == rootQ:
            return
        self.parent[rootQ] = rootP
        self.count -= 1


class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        n = len(row)
        uf = UF(n)

        for i in range(0, n, 2):
            uf.parent[i + 1] = i
            uf.count -= 1

        for i in range(0, n, 2):
            if (row[i] % 2 == 0 and row[i + 1] == row[i] + 1) or (row[i + 1] % 2 == 0 and row[i] == row[i + 1] + 1):
                pass
            else:
                uf.union(row[i], row[i + 1])

        return n // 2 - uf.count