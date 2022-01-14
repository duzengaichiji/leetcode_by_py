class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        idx = 0
        for i in range(len(nums)):
            if nums[i]>0:
                nums[idx] = nums[i]
                idx+=1
        nums = nums[:idx]
        if len(nums)==0:
            return 1
        n = len(nums)
        for i in range(n):
            if abs(nums[i])<=n:
                nums[abs(nums[i])-1] = -nums[abs(nums[i])-1] \
                    if nums[abs(nums[i])-1]>0 else nums[abs(nums[i])-1]
        print(nums)
        for i in range(n):
            if nums[i]>0:
                return i+1
        return n+1