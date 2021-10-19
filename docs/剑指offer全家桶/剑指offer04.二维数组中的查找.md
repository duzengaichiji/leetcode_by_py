剑指offer04.二维数组中的查找
----------
 - 题目
>在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个高效的函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
 - 示例
 ----------
>input:
>
> 
[[1,   4,  7, 11, 15],
>
  [2,   5,  8, 12, 19],
>
  [3,   6,  9, 16, 22],
>
  [10, 13, 14, 17, 24],
>
  [18, 21, 23, 26, 30]
>
], target=5
>
>
> output: true 
 ----------
 - 代码
 > dfs+回溯
>
    class Solution:
        def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
            def backtrack(matrix,target,used,row,col):
                print(row,col)
                if matrix[row][col]==target:
                    return True
                left = False
                # 向右搜索
                if row<len(matrix)-1 and used[row+1][col]==False and matrix[row+1][col]<=target:
                    used[row+1][col] = True
                    left = backtrack(matrix,target,used,row+1,col)
                right = False
                # 向下搜索
                if col<len(matrix[0])-1 and used[row][col+1]==False and matrix[row][col+1]<=target:
                    used[row][col+1] = True
                    right = backtrack(matrix,target,used,row,col+1)
                return left|right
            used = [[False]*len(matrix[0]) for _ in range(len(matrix))]
            if len(matrix)==0 or len(matrix[0])==0:
                return False
            return backtrack(matrix,target,used,0,0)
>
> 贪心算法
>
    class Solution:
        def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
            if not matrix: return False
            m = len(matrix)
            n = len(matrix[0])
            # 从右上角开始搜索
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
 ----------
 - 解析
 >
> 由于矩阵的性质，每个元素一定大于其 上，左 的元素；
>
> 因此如果从【0，0】开始，沿着 下，右两个方向进行dfs搜索就可以了；
>
 ----------
> 由于数组的特殊性，某个位置(i,j)的下面(x,y,y>j)以及右面元素(x,y,x>i)都大于这个数，相反，该位置左边和上面的元素都比该元素小；
>
> 因此，如果 当前查找数>target，则target一定出现该数的**左边**范围，因为该数的右下范围都比该数大，因此往左移动；
>
> 如果 当前查找数<target，则target一定出现在**右边**范围，因为该数的左上角都比该数小，因此向下移动；
>
> 而如何排除该数的**右上**范围， 就要求从数组的右上角开始搜索，一开始的数字没有右上范围，因此在搜索过程中，任意数字的右上范围已经被排除；
>
> 同理，从数组的左下角开始搜索，同样可行；