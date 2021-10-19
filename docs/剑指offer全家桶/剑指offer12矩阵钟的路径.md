剑指offer12.矩阵中的路径
----------
 - 题目
>请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。路径可以从矩阵中的任意一格开始，每一步可以在矩阵中向左、右、上、下移动一格。如果一条路径经过了矩阵的某一格，那么该路径不能再次进入该格子。例如，在下面的3×4的矩阵中包含一条字符串“bfce”的路径（路径中的字母用加粗标出）。
>
[["a",**"b"**,"c","e"],
>
["s",**"f"**,**"c"**,"s"],
>
["a","d","e",**"e"**]]
>
>
> 但矩阵中不包含字符串“abfb”的路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入这个格子。

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
            row = len(board)
            col = len(board[0])
            def dfs(r,c,index,used):
                if r<0 or r>=row or c<0 or c>=col:
                    return False
                if used[r][c]:
                    return False
                char = word[index]
                used[r][c] = True
                res = False
                if board[r][c]==char:
                    if index==len(word)-1:
                        return True
                    res = dfs(r-1,c,index+1,used) \
                    or dfs(r+1,c,index+1,used) \
                    or dfs(r,c-1,index+1,used) \
                    or dfs(r,c+1,index+1,used)
                used[r][c] = False
                return res
            used = [[False]*col for _ in range(row)]
            for i in range(row):
                for j in range(col):
                    if dfs(i,j,0,used):
                        return True
            return False
 ----------
 - 解析
 > 每个点来一次dfs，看其有没有可行路径