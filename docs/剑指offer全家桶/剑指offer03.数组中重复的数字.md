剑指offer03.数组中重复的数字
----------
 - 题目
>找出数组中重复的数字。
>
> 在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。

 - 示例
 ----------
>input: [2, 3, 1, 0, 2, 5, 3]

> output: 2 或 3 
 ----------
 - 代码
 >
>
    class Solution:
        def findRepeatNumber(self, nums: List[int]) -> int:
            count = collections.Counter(nums)
            for key,value in count.items():
                if value>1:
                    return key
            return 0
 ----------
 - 解析
 > 没什么好说的。。哈希表计数