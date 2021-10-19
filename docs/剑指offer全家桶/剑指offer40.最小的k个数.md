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
>  直接排序
>
    class Solution:
        def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
            arr = sorted(arr)
            return arr[:k]
>
>
> 快速选择算法
>
    class Solution:
        def smallestK(self, arr: List[int], k: int) -> List[int]:
            # 快速排序的分配过程
            def fastSearch(arr,start,end,k):
                inc = arr[start]
                left = start
                right = end
                while left<right:
                    while left<right and arr[right]>=inc:
                        right-=1
                    if left<right:
                        arr[left] = arr[right]
                        left+=1
                    while left<right and arr[left]<inc:
                        left+=1
                    if left<right:
                        arr[right] = arr[left]
                        right-=1
                arr[right] = inc
                return right
            start = 0
            end = len(arr)-1
            k_ = k
            while k>0:
                # 找到分割点的位置
                cur = fastSearch(arr,start,end,k)
                # 如果分割点>k，则前k个数均在左半边；
                # 此时将搜索空间压缩到分割点前面
                if (cur-start+1)>k:
                    end = cur-1
                # 如果分割点<k，则前k个数在分割点左边和右边均有分布
                # 因此去掉左半边之后，将k减小，
                # 在右半边搜索剩下的数；
                elif (cur-start+1)<k:
                    k-=(cur-start+1)
                    start = cur+1
                # 找到topk的位置了，此时返回前k个数即可
                elif (cur-start+1)==k:
                    k = 0
            return arr[:k_]
  ----------
 - 解析
 > 选择直接排序，取前k个，复杂度为O(nlogn)
 > 
> 可以使用堆排序，进行k轮即可，即一轮建堆，k轮调整；
> 
> 也可以用快速选择算法；
>
  ----------
 > 快速选择算法基于快速排序，可以用来解决topk类型的问题；
>
> 总体思想和快速排序类似；
>
> 在快速排序的每一轮之后，会确定分割点（inc）所在的位置；
>
> 当该位置大于k时，则topk在该位置的左半边，可以舍弃右半边，同理，位置大于k时候可以舍弃左半边；
>
> 这样当某轮排序之后，分割点恰好能等于topk；
>
> 该题中，要取前k个则同理，只是在分割点位置小于k时，不能舍弃左半边；
> 
> 具体区别可以看注释；