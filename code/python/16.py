class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        res = float('inf')
        for i in range(len(nums)-1):
            if i>0 and nums[i]==nums[i-1]: continue
            l = i+1
            r = len(nums)-1
            while l<r:
                s = nums[i]+nums[l]+nums[r]
                if abs(s-target)<abs(res-target): res = s
                if s>target:
                    while l<r and nums[r]==nums[r-1]:
                        r-=1
                    r-=1
                else:
                    while l<r and nums[l]==nums[l+1]:
                        l+=1
                    l+=1
        return res