class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        def maxProfitForK(prices,k):
            dp_i_0 = [0]*(k+1)
            dp_i_1 = [float('-inf')]*(k+1)
            for price in prices:
                for i in range(1,k+1):
                    dp_i_0[i] = max(dp_i_0[i],dp_i_1[i]+price)
                    dp_i_1[i] = max(dp_i_1[i],dp_i_0[i-1]-price)
            return dp_i_0[-1]
        def maxProfitForUnlimit(prices):
            dp_i_0 = 0
            dp_i_1 = float('-inf')
            for price in prices:
                temp = dp_i_0
                dp_i_0 = max(dp_i_0,dp_i_1+price)
                dp_i_1 = max(dp_i_1,temp-price)
            return dp_i_0
        if k>=len(prices)//2:
            return maxProfitForUnlimit(prices)
        else:
            return maxProfitForK(prices,k)