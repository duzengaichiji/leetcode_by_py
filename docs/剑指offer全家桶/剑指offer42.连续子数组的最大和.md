剑指offer42.连续子数组的最大和
----------
 - 题目
>输入一个整型数组，数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。
>
> 要求时间复杂度为O(n)。
> 
 - 示例
 ----------
> input: nums = [-2,1,-3,4,-1,2,1,-5,4]
> 
> output: 6
 ----------
 - 代码
 >
>
    class Solution:
        def maxSubArray(self, nums: List[int]) -> int:
            temp = -float('inf')
            res = -float('inf')
            for num in nums:
                # 如果累计和没有当前数字大，那么从当前数字开始重新累计
                temp = max(temp+num,num)
                res = max(temp,res)
            return res
  ----------
 - 解析
 > 