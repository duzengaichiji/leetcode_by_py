class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp_i_1 = 0#当前第i间偷
        dp_i_2 = 0#当前第i间不偷
        for i in range(n):
            temp = dp_i_2
            dp_i_2 = max(dp_i_2,dp_i_1)
            dp_i_1 = temp+nums[i]
        return max(dp_i_2,dp_i_1)