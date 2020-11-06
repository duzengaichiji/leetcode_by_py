class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        n = len(nums)
        summation = sum(nums)
        if abs(summation)<abs(S): return 0
        #要把-summation包括进去，所以使用2*summation表示-summation---summation
        length = 2*summation+1
        dp = [[0]*length for _ in range(n)]
        dp[0][summation+nums[0]] = 1
        dp[0][summation-nums[0]] +=1
        for i in range(1,n):
            for j in range(length):
                #从大数-nums[i]到达j,从小数+nums[i]到达j
                l = dp[i-1][j-nums[i]] if 0<=j-nums[i]<length else 0
                r = dp[i-1][j+nums[i]] if 0<=j+nums[i]<length else 0
                dp[i][j] = l+r
        #由于从-summation开始表示，所以summation+S才是+S
        return dp[-1][summation+S]