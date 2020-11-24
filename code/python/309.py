class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp_i_0 = 0
        dp_i_1 = float('-inf')
        dp_i_0_1 = 0
        dp_i_1_1 = float('-inf')
        for price in prices:
            temp_0 = dp_i_0
            temp_1 = dp_i_1
            dp_i_0 = max(dp_i_0,dp_i_1+price)
            dp_i_1 = max(dp_i_1,dp_i_0_1-price)
            dp_i_0_1 = temp_0
            dp_i_1_1 = temp_1
            #print(dp_i_0,dp_i_1)
        return dp_i_0