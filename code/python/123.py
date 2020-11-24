class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def maxProfitForK(prices,k):
            dp_i_0 = [0]*(k+1)#每一天交易k次的时候，当前未持有股票能获得的最大利润
            dp_i_1 = [-float('inf')]*(k+1)#每一天k次。。。
            for price in prices:
                for i in range(1,k+1):
                    dp_i_0[i] = max(dp_i_0[i],dp_i_1[i]+price)
                    dp_i_1[i] = max(dp_i_1[i],dp_i_0[i-1]-price)
            return dp_i_0[-1]
        return maxProfitForK(prices,2)