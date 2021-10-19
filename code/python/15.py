class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums)<3:
            return []
        nums = sorted(nums)
        ans = []
        for i in range(len(nums)):
            if nums[i]>0:
                break
            if i>0 and nums[i]==nums[i-1]:#重复，略过
                continue
            l = i+1
            r = len(nums)-1
            while l<r:
                s = nums[l]+nums[r]+nums[i]
                if s==0:
                    ans.append(sorted([nums[l],nums[r],nums[i]]))
                    while l<r and nums[l]==nums[l+1]:#去重之后，后推一位，再看是否还存在解
                        l+=1
                    while l<r and nums[r]==nums[r-1]:
                        r-=1
                    l+=1
                    r-=1
                elif s<0:
                    l+=1
                elif s>0:
                    r-=1
        return ans