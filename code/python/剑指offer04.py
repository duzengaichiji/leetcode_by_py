class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        def backtrack(matrix,target,used,row,col):
            print(row,col)
            if matrix[row][col]==target:
                return True
            left = False
            if row<len(matrix)-1 and used[row+1][col]==False and matrix[row+1][col]<=target:
                used[row+1][col] = True
                left = backtrack(matrix,target,used,row+1,col)
            right = False
            if col<len(matrix[0])-1 and used[row][col+1]==False and matrix[row][col+1]<=target:
                used[row][col+1] = True
                right = backtrack(matrix,target,used,row,col+1)
            return left|right
        used = [[False]*len(matrix[0]) for _ in range(len(matrix))]
        if len(matrix)==0 or len(matrix[0])==0:
            return False
        return backtrack(matrix,target,used,0,0)