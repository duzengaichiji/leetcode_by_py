剑指offer57.和为s的两个数字
----------
 - 题目
>输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们的和正好是s。如果有多对数字的和等于s，则输出任意一对即可。

 - 示例
 ----------
>input: nums = [2,7,11,15], target = 9

> output: [2,7]
 ----------
 - 代码
 >
>
    class Solution:
        def twoSum(self, nums: List[int], target: int) -> List[int]:
            nums = sorted(nums)
            i = 0
            j = len(nums)-1
            while nums[i]+nums[j]!=target:
                if nums[i]+nums[j]<target:
                    i+=1
                else:
                    j-=1
            return [nums[i],nums[j]]
 ----------
 - 解析
> 排序可以将暴力求解的复杂度变小;