class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)<1:
            return 0
        result = 0
        min_val = prices[0]
        for i in range(1,len(prices)):
            if prices[i]-min_val>result:
                result = prices[i]-min_val
            if prices[i]<min_val:
                min_val=prices[i]
        return result