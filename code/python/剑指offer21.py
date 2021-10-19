class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        if len(nums)==0:
            return nums
        inc = nums[0]
        start = 0
        end = len(nums)-1
        while start<end:
            while start<end and nums[end]%2==0:
                end-=1
            if start<end:
                nums[start]=nums[end]
                start+=1
            while start<end and nums[start]%2!=0:
                start+=1
            if start<end:
                nums[end] = nums[start]
                end-=1
        nums[end] = inc
        return nums