class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        ans = []
        # 第一个子数组和，第一个子数组的最大和，前者的起始位置
        sum1, maxSum1, maxSum1Idx = 0, 0, 0
        # 第二个子数组和，前两个子数组的最大和，两者的起始位置
        sum2, maxSum12, maxSum12Idx = 0, 0, ()
        # 第三个子数组和，三者的最大和
        sum3, maxTotal = 0, 0
        #
        for i in range(k * 2, len(nums)):
            # 在i到达3k-1之前，其实算的是第一份子数组和
            # sum1=sum(nums[:k]), sum2=sum(nums[k:2*k])..
            sum1 += nums[i - k * 2]
            sum2 += nums[i - k]
            sum3 += nums[i]
            # 更新过程
            if i >= 3 * k - 1:
                if sum1 > maxSum1:
                    maxSum1 = sum1
                    # 记录第一个子数组的起始位置
                    maxSum1Idx = i - 3 * k + 1
                if maxSum1 + sum2 > maxSum12:
                    maxSum12 = maxSum1 + sum2
                    maxSum12Idx = (maxSum1Idx, i - k * 2 + 1)
                if maxSum12 + sum3 > maxTotal:
                    maxTotal = maxSum12 + sum3
                    ans = [*maxSum12Idx, i - k + 1]
                # 三个子数组向前移动
                sum1 -= nums[i - k * 3 + 1]
                sum2 -= nums[i - k * 2 + 1]
                sum3 -= nums[i - k + 1]
        return ans
