class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        length = len(nums)
        if length==0: return False
        total = sum(nums)
        if total%2!=0: return False

        target = total//2
        dp = [[False]*(target+1) for _ in range(length)]
        if nums[0]<=target:
            dp[0][nums[0]] = True

        for i in range(length):
            for j in range(target+1):
                dp[i][j] = dp[i-1][j]
                if nums[i]==j:
                    dp[i][j] = True
                    continue
                if nums[i]<j:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i]]
        return dp[-1][-1]