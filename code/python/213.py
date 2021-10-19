class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==0: return 0
        if len(nums)<=2: return max(nums)
        def robMax(arr,start,end):
            dp_i_0 = 0
            dp_i_1 = 0
            temp = 0
            for i in range(start,end):
                temp = dp_i_1
                dp_i_1 = max(dp_i_0,dp_i_1)
                dp_i_0 = temp+nums[i]
            return max(dp_i_0,dp_i_1)
        n = len(nums)
        return max(robMax(nums,0,n-1),robMax(nums,1,n))