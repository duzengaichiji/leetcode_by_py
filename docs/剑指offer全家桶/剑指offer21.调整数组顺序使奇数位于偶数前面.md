剑指offer21.调整数组顺序使奇数位于偶数前面
----------
 - 题目
>输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分
 - 示例
 ----------
>input: [1,2,3,4]

> output: [1,3,2,4]
 ----------
 - 代码
 >
>
    class Solution:
        def exchange(self, nums: List[int]) -> List[int]:
            if len(nums)==0:
                return nums
            inc = nums[0]
            start = 0
            end = len(nums)-1
            while start<end:
                while start<end and nums[end]%2==0:
                    end-=1
                if start<end:
                    nums[start]=nums[end]
                    start+=1
                while start<end and nums[start]%2!=0:
                    start+=1
                if start<end:
                    nums[end] = nums[start]
                    end-=1
            nums[end] = inc
            return nums
  ----------
 - 解析
 > 
> 快速排序的思想；
> 
> 一轮O(n)即可将奇数放在前面，偶数放在后面；