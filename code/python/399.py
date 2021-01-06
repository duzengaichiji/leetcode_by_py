class UF:
    def __init__(self,n):
        self.parent = [i for i in range(n)]
        self.values = [1]*n
    def find(self,x):
        if x!=self.parent[x]:
            origin = self.parent[x]
            self.parent[x] = self.find(self.parent[x])
            self.values[x]*=self.values[origin]
        return self.parent[x]
    def union(self,x,y,value):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX==rootY:
            return
        self.parent[rootX] = rootY
        self.values[rootX] = self.values[y]*value/self.values[x]
    def isConnected(self,x,y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX==rootY:
            return self.values[x]/self.values[y]
        return -1
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        charIndex = {}
        uf = UF(len(equations)*2)
        index = 0
        for i in range(len(equations)):
            var1 = equations[i][0]
            var2 = equations[i][1]
            if var1 not in charIndex:
                charIndex[var1] = index
                index+=1
            if var2 not in charIndex:
                charIndex[var2] = index
                index+=1
            uf.union(charIndex[var1],charIndex[var2],values[i])
        res = []
        for i in range(len(queries)):
            var1 = queries[i][0]
            var2 = queries[i][1]

            if var1 not in charIndex or var2 not in charIndex:
                res.append(-1)
                continue
            res.append(uf.isConnected(charIndex[var1],charIndex[var2]))
        return res