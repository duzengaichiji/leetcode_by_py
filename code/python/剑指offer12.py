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