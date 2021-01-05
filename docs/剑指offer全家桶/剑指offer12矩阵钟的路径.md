剑指offer12.矩阵中的路径
----------
 - 题目
>请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。路径可以从矩阵中的任意一格开始，每一步可以在矩阵中向左、右、上、下移动一格。如果一条路径经过了矩阵的某一格，那么该路径不能再次进入该格子。例如，在下面的3×4的矩阵中包含一条字符串“bfce”的路径（路径中的字母用加粗标出）。

[["a","b","c","e"],
["s","f","c","s"],
["a","d","e","e"]]

但矩阵中不包含字符串“abfb”的路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入这个格子。

----------
 - 示例
> input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
>
> output:true
 ----------
 - 代码
 >
>
    class Solution:
        def exist(self, board: List[List[str]], word: str) -> bool:
            def backtrack(index,length,i,j,row,col,used):
                if index==length:
                    return True
                direction = [(-1,0),(1,0),(0,-1),(0,1)]
                res = False
                for d in direction:
                    if i+d[0]>=0 and i+d[0]<row and j+d[1]>=0 and j+d[1]<col:
                        if board[i+d[0]][j+d[1]]==word[index] and used[i+d[0]][j+d[1]]==False:
                            used[i+d[0]][j+d[1]] = True
                            res = res or backtrack(index+1,length,i+d[0],j+d[1],row,col,used)
                            used[i+d[0]][j+d[1]] = False
                return res
    
            row = len(board)
            col = len(board[0])
            length = len(word)
            for i in range(row):
                for j in range(col):
                    if board[i][j]==word[0]:
                        used = [[False]*col for _ in range(row)]
                        used[i][j] = True
                        if backtrack(1,length,i,j,row,col,used)==True:
                            return True
    
            return False
 ----------
 - 解析
 > 每个点来一次dfs，看其有没有可行路径