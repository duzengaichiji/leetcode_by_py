剑指offer41.数据流的中位数
----------
 - 题目
>如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。
>
>例如，
>
>[2,3,4] 的中位数是 3
>
>[2,3] 的中位数是 (2 + 3) / 2 = 2.5
>
>设计一个支持以下两种操作的数据结构：
>
>void addNum(int num) - 从数据流中添加一个整数到数据结构中。
> 
>double findMedian() - 返回目前所有元素的中位数。
> 
 - 示例
 ----------
> input: ["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]
> 
> [[],[1],[2],[],[3],[]]
> 
> output: [null,null,null,1.50000,null,2.00000]
 ----------
 - 代码
 >
>
    import bisect
    class MedianFinder:
    
        def __init__(self):
            """
            initialize your data structure here.
            """
            self.arr = []
    
    
        def addNum(self, num: int) -> None:
            if not self.arr:
                self.arr.append(num)
            else:
                index = bisect.bisect_left(self.arr,num)
                self.arr.insert(index,num)
            
    
        def findMedian(self) -> float:
            if len(self.arr)%2!=0:
                return self.arr[len(self.arr)//2]
            else:
                return (self.arr[len(self.arr)//2]+self.arr[len(self.arr)//2-1])/2
    
    
    # Your MedianFinder object will be instantiated and called as such:
    # obj = MedianFinder()
    # obj.addNum(num)
    # param_2 = obj.findMedian()
>
>  解法二
> 
    from heapq import *
    class MedianFinder:
    
        def __init__(self):
            """
            initialize your data structure here.
            """
            self.A = []
            self.B = []
    
    
        def addNum(self, num: int) -> None:
            if len(self.A)!=len(self.B):
                heappush(self.A,num)
                heappush(self.B,-heappop(self.A))
            else:
                heappush(self.B,-num)
                heappush(self.A,-heappop(self.B))
        def findMedian(self) -> float:
            return self.A[0] if len(self.A)!=len(self.B) else (self.A[0]-self.B[0])/2.0
    
    
    # Your MedianFinder object will be instantiated and called as such:
    # obj = MedianFinder()
    # obj.addNum(num)
    # param_2 = obj.findMedian()
  ----------
 - 解析
 > 最简单的做法，就是每次插入之后，都保证当前存储的数组是有序的，如此，取到中位数很容易；
 > 
> 针对 当前存储的数组是有序的 这件事，有简化策略；
> 
> 将存储的数组整体分为两个部分：A，B；
> 
> A为一个小顶堆，B为一个大顶堆；
> 
> 其中，A的所有元素都大于B的最大元素；
> 
> 这样，中位数只会与 A的堆顶以及B的堆顶有关联；
> 
> 保持A的小顶堆属性，B的小顶堆属性，以及两个堆的数量成了关键；
> 
  ----------
> 如果当前A的长度与B的相等，我们希望多出来的那个元素给B（也可以给A）；
> 
> 则 **需要将待插入的元素插入A，并且将A的最小元素推给B**；
> 
> 反之一样，要插入A时，需要先插入B，然后将B中的最大元素推给A；
> 
> 
    if len(self.A)!=len(self.B):
        heappush(self.A,num)
        heappush(self.B,-heappop(self.A))
    else:
        heappush(self.B,-num)
        heappush(self.A,-heappop(self.B))
> 
> 由于python默认只有小顶堆，因此要建立大顶堆时，必须用负数来进行反向小顶堆；