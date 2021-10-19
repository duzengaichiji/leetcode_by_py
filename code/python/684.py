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
        # 该边能够构成环
        if rootP == rootQ:
            return False
        self.parent[rootP] = rootQ
        self.count -= 1
        return True

    def divide(self, p, q):
        pass


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UF(len(edges))
        for edge in edges:
            x, y = edge
            if uf.union(x - 1, y - 1) == False:
                return edge