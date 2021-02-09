剑指offer40.最小的k个数
----------
 - 题目
>输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。
> 
 - 示例
 ----------
> input: arr = [3,2,1], k = 2
> 
> output: [1,2] 或者 [2,1]
 ----------
 - 代码
 >
>
    class Solution:
        def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
            arr = sorted(arr)
            return arr[:k]
  ----------
 - 解析
 > 选择直接排序，取前k个，复杂度为O(nlogn)
 > 
> 可以使用堆排序，进行k轮即可，即一轮建堆，k轮调整；
> 
> 也可以用快速选择算法；