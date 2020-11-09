class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        dp = [0]*(len(arr)+1)
        for i in range(1,len(arr)+1):
            j = i-1
            mx = -float('inf')
            # 最长为K的字数组
            while i-j<=k and j>=0:
                mx = max(mx,arr[j])
                dp[i] = max(dp[i],dp[j]+mx*(i-j))
                j-=1
        return dp[-1]