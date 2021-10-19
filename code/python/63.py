class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0]==1:
            return 0
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        dp = [[0]*col for _ in range(row)]
        for i in range(row):
            if obstacleGrid[i][0]==0:
                dp[i][0] = 1
            else:
                break
        for i in range(col):
            if obstacleGrid[0][i]==0:
                dp[0][i] = 1
            else:
                break
        for i in range(1,row):
            for j in range(1,col):
                if obstacleGrid[i][j]==0:
                    dp[i][j] = dp[i-1][j]+dp[i][j-1]
        #print(dp)
        return dp[-1][-1]