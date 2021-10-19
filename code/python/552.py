class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 1000000007
        # 第i天，缺席j次，迟到k次的可行序列数量
        dp = [0]*6
        dp[0] = 1
        dp[1] = 1
        dp[3] = 1
        for i in range(1,n):
            newDp = [0]*6
            newDp[0] = (dp[0] + dp[1] + dp[2]) % MOD;
            newDp[1] = dp[0];
            newDp[2] = dp[1];
            newDp[3] = (dp[3] + dp[4] + dp[5] + dp[0] + dp[1] + dp[2]) % MOD;
            newDp[4] = dp[3];
            newDp[5] = dp[4];
            dp = newDp
        return sum(dp)%MOD