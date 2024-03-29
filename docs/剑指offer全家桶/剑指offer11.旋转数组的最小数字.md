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
> 使用2分查找的目的是缩小搜索范围，将复杂度减小到O(logn)级；
>
> 我们分为两种情况，一种是整个数组顺序排列的情况，一种是存在旋转的情况；
>
> 首先，每次二分的过程中，总会对比 low,pivot,high这三个位置上的数；
>
> 如果数组存在旋转，则 **最小值一定位于乱序列的那一半** 
>
> （以[3,4,5,1,2]为例，显然，有序的那一半[3,4]可以被排除；)
>
> 所以先判定右半是否有序，如果有，则排除它们（pivot位置上的值是可能成为最小的，比如[4,5,1,2,3])
>
> 相反，如果右边无序，则可以排除左边（此时pivot不可能是最小的，因为numbers[pivot]>numbers[higjh])
>
> 至于相等的情况，则可以直接忽略最右边的值，毕竟他都和pivot相等了；
>
 ----------
> 那么，为什么不使用左边界作为对比参考？
>
> 比如 numbers[pivot]>numbers[low]作为分支条件；
>
>原因在于，确定左边是顺序的时候，是无法确定最小值所在的范围的，比如（[1,2,3,4,5],[3,4,5,1,2]都属于左边顺序的情况）；
>
> 而左边乱序的情况，又可以通过右边顺序的情况来覆盖；