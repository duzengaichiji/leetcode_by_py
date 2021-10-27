class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        f = [0]*len(nums)
        g = [0]*len(nums)
        maxLen = -1
        for i in range(len(nums)):
            f[i] = 1
            g[i] = 1
            for j in range(i):
                if nums[j]<nums[i]:
                    # 以nums[i]为结尾的最长子序列变更
                    if f[i]<f[j]+1:
                        f[i] = f[j]+1
                        g[i] = g[j]
                    # 有新的长度为f[i]的子序列
                    elif f[i]==f[j]+1:
                        g[i] += g[j]
            maxLen = max(maxLen,f[i])
        ans = 0
        for i in range(len(nums)):
            if f[i]==maxLen:
                ans+=g[i]
        return ans