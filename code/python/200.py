class UF:
    def __init__(self,count):
        self.count = count
        self.parent = [i for i in range(count)]
    def find(self,x):
        while x!=self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    def union(self,p,q):
        rootP = self.find(p)
        rootQ = self.find(q)
        if rootP==rootQ:
            return
        self.parent[rootQ] = rootP
        self.count-=1

class Solution:
    def numIslands(self, grid) -> int:
        row = len(grid)
        col = len(grid[0])

        uf = UF(row*col)
        for i in range(row):
            for j in range(col):
                if grid[i][j]=='0':
                    uf.parent[i*col+j] = -1
                    uf.count-=1

        for i in range(row):
            for j in range(col):
                if grid[i][j]=='1':
                    grid[i][j] = '0'
                    direction = [(-1,0),(1,0),(0,-1),(0,1)]
                    for d in direction:
                        if i+d[0]>=0 and i+d[0]<row and j+d[1]>=0 and j+d[1]<col and grid[i+d[0]][j+d[1]]=='1':
                            uf.union(i*col+j,(i+d[0])*col+(j+d[1]))
        return uf.count