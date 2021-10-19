剑指offer46.把数字翻译成字符串
----------
 - 题目
>给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。一个数字可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。
> 
 - 示例
 ----------
> input: 12258
> 
> output: 5
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