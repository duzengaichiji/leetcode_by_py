class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums: return 0
        l = 0
        r = len(nums)-1
        while l<=r:
            mid = (l+r)//2
            if nums[mid]<target:
                l = mid+1
            elif nums[mid]>target:
                r = mid-1
            else:
                break
        if l>r: return 0
        l = mid
        r = mid
        while l>=0 and nums[l]==nums[mid]: l-=1
        while r<len(nums) and nums[r]==nums[mid]: r+=1
        return r-l-1