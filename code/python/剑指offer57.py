class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums = sorted(nums)
        i = 0
        j = len(nums)-1
        while nums[i]+nums[j]!=target:
            if nums[i]+nums[j]<target:
                i+=1
            else:
                j-=1
        return [nums[i],nums[j]]