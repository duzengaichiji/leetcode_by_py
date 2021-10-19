class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return []
        l,r,u,d = 0,len(matrix[0])-1,0,len(matrix)-1
        res = []
        while True:
            for i in range(l,r+1):
                res.append(matrix[u][i])
            u+=1
            if u>d: break
            for i in range(u,d+1):
                res.append(matrix[i][r])
            r-=1
            if l>r: break
            for i in range(r,l-1,-1):
                res.append(matrix[d][i])
            d-=1
            if u>d: break
            for i in range(d,u-1,-1):
                res.append(matrix[i][l])
            l+=1
            if l>r: break
        return res