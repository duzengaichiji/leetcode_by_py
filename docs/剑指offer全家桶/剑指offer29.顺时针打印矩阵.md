剑指offer29.顺时针打印矩阵
----------
 - 题目
>输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字
 - 示例
 ----------
>input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
> 
> output: [1,2,3,6,9,8,7,4,5]
 ----------
 - 代码
 >
>
    class Solution:
        def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
            if not matrix: return []
            l,r,u,d = 0,len(matrix[0])-1,0,len(matrix)-1
            res = []
            while True:
                # 上
                for i in range(l,r+1):
                    res.append(matrix[u][i])
                u+=1
                if u>d: break
                # 右
                for i in range(u,d+1):
                    res.append(matrix[i][r])
                r-=1
                if l>r: break
                # 下
                for i in range(r,l-1,-1):
                    res.append(matrix[d][i])
                d-=1
                if u>d: break
                # 左
                for i in range(d,u-1,-1):
                    res.append(matrix[i][l])
                l+=1
                if l>r: break
            return res
  ----------
 - 解析
 > 
> 