剑指offer39.数组中出现次数超过一半的数字
----------
 - 题目
>数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
> 
> 你可以假设数组是非空的，并且给定的数组总是存在多数元素
 - 示例
 ----------
> input: [1, 2, 3, 2, 2, 2, 5, 4, 2]
> 
> output: 2
 ----------
 - 代码
 >
>
    class Solution:
        def majorityElement(self, nums: List[int]) -> int:
            count = collections.Counter(nums)
            for key,value in count.items():
                if value>len(nums)//2:
                    return key
  ----------
 - 解析
 > 哈希表的简单应用