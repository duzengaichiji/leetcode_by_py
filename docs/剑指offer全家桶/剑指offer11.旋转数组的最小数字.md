剑指offer11.旋转数组的最小数字
----------
 - 题目
>把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。 
>
----------
 - 示例
> input: [3,4,5,1,2]
>
> output: 1
 ----------
 - 代码
 > 
> 
>
    class Solution:
        def minArray(self, numbers: List[int]) -> int:
            low, high = 0, len(numbers) - 1
            while low < high:
                pivot = low + (high - low) // 2
                # 右边有序，找左边
                if numbers[pivot] < numbers[high]:
                    high = pivot
                # 左边有序，找右边 (此时numbers[pivot]可以确定不是最小值)
                elif numbers[pivot] > numbers[high]:
                    low = pivot + 1
                # 很多重复元素，直接改变pivot的位置，继续二分
                else:
                    high -= 1
            return numbers[low]
 ----------
 - 解析
> 二分查找;