class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix: return False
        m = len(matrix)
        n = len(matrix[0])
        i = 0
        j = n-1
        while i>=0 and i<m and j>=0 and j<n:
            if matrix[i][j]>target:
                j-=1
            elif matrix[i][j]<target:
                i+=1
            else:
                return True

        return False