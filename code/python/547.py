class UF:
    def __init__(self,count):
        self.count = count
        self.parent = [0]*count
        self.size = [1]*count
        for i in range(count):
            self.parent[i] = i

    def union(self,p,q):
        rootP = self.find(p)
        rootQ = self.find(q)
        if rootP==rootQ:
            return
        if self.size[rootP]>self.size[rootQ]:
            self.parent[rootQ] = rootP
            self.size[rootP]+=self.size[rootQ]
        else:
            self.parent[rootP] = rootQ
            self.size[rootQ]+=self.size[rootP]
        self.count-=1

    def connected(self,p,q):
        rootP = self.find(p)
        rootQ = self.find(q)
        return rootP==rootQ

    def find(self,x):
        while self.parent[x]!=x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        n = len(M)
        uf = UF(n)
        for i in range(n):
            for j in range(i):
                if M[i][j]==1:
                    uf.union(i,j)
        return uf.count