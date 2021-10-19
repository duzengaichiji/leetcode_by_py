class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        temp = -float('inf')
        res = -float('inf')
        for num in nums:
            temp = max(temp+num,num)
            res = max(temp,res)
        return res