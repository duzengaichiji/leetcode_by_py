class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for num in range(coin,amount+1):
                dp[num] = min(dp[num],dp[num-coin]+1)
        print(dp)
        return dp[-1]