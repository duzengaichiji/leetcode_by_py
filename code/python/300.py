class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = [1]*len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i]>nums[j]:
                    res[i] = max(res[i],res[j]+1)
                elif nums[i]==nums[j]:
                    res[i] = res[j]
        return max(res)