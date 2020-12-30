剑指offer04.二维数组中的查找
----------
 - 题目
>在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个高效的函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
 - 示例
 ----------
>input: [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
], target=5

> output: true 
 ----------
 - 代码
 >
>
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
 ----------
 - 解析
 >
>