class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        changed = []
        row, col = len(board), len(board[0])

        def live_or_die(x, y):
            live_neighors = 0
            for d in [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]:
                if 0 <= x + d[0] < row and 0 <= y + d[1] < col:
                    live_neighors += board[x + d[0]][y + d[1]]
            # 四条规则
            if board[x][y] == 1:
                if live_neighors < 2:
                    return False
                if live_neighors > 3:
                    return False
                return True
            else:
                if live_neighors == 3:
                    return False
                return True

        for i in range(row):
            for j in range(col):
                if not live_or_die(i, j):
                    changed.append((i, j))

        for i, j in changed:
            board[i][j] = 1 - board[i][j]