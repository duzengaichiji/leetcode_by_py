剑指offer47.礼物的最大价值
----------
 - 题目
>在一个 m*n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于 0）。你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格、直到到达棋盘的右下角。给定一个棋盘及其上面的礼物的价值，请计算你最多能拿到多少价值的礼物？
 - 示例
 ----------
> input: [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
> 
> output: 12
 ----------
 - 代码
 >
>
    class Solution:
        def maxValue(self, grid: List[List[int]]) -> int:
            if not grid: return 0
            row = len(grid)
            col = len(grid[0])
            dp = [[0]*col for _ in range(row)]
            dp[0][0] = grid[0][0]
            for i in range(1,row):
                dp[i][0] = dp[i-1][0]+grid[i][0]
            for j in range(1,col):
                dp[0][j] = dp[0][j-1]+grid[0][j]
            
            for i in range(1,row):
                for j in range(1,col):
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])+grid[i][j]
            return dp[-1][-1]
  ----------
 - 解析
 > 
> 简单dp，由于每个点可以由其上面一个或者左边一个移动过来，因此，只要选择上面一个或者左边一个中更大的那个结果就行；
>
> dp[i][j]表示，在点(i,j)处获得的礼物最大价值；
>
> （可以参考编辑距离，一样的道理）