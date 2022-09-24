剑指offer67.把字符串转换为整数
----------
 - 题目
>给定一个数组 nums 和滑动窗口的大小 k，请找出所有滑动窗口里的最大值。

 - 示例
 ----------
>input: nums = [1,3,-1,-3,5,3,6,7], k=3

> output: [3,3,5,5,6,7]
 ----------
 - 代码
 > 方法一.单调队列
>
    class Solution:
     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
         deque = []
         window = []
         n = len(nums)
         for i in range(min(n,k)):
             window.append(nums[i])
             if not deque or nums[i]<=deque[-1]:
                 deque.append(nums[i])
             else:
                 while deque and nums[i]>deque[-1]:
                     deque.pop()
                 deque.append(nums[i])
 
         res = []
         res.append(deque[0])
 
         for i in range(k,n):
             num = nums[i]
             if not deque or num<=deque[-1]:
                 deque.append(num)
             else:
                 while deque and num>deque[-1]:
                     deque.pop()
                 deque.append(num)
             popd = nums[i-k]
             if popd==deque[0]:
                 deque = deque[1:]
             res.append(deque[0])
         return res
>
> 方法二. 堆
>
> 
    import heapq
      class Solution:
          def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
              n = len(nums)
              q = [(-nums[i],i) for i in range(min(n,k))]
              heapq.heapify(q)
      
              ans = [-q[0][0]]
              for i in range(k,n):
                  heapq.heappush(q,(-nums[i],i))
                  # 移除不在窗口中的最大值
                  while q[0][1]<=i-k:
                      heapq.heappop(q)
                  ans.append(-q[0][0])
              return ans
              
 ----------
 - 解析
 > 方法一很大程度上参考 59-2 的解；
> 
> 简单来说就是用这个单调队列去维护最大值，至于为什么用不了单调栈，因为滑动窗口的时候，**总是先进入窗口的数字先被踢**，**所以使用的数据结构要保持这一特性**
 > 
> 至于方法二
> 
> 这里需要明白的一个问题，就是最大值不受已不在窗口中的非最大值的影响；
> 
> 以例子中的数字为例；
> 
> 当窗口移动到 [3,-1,-3]时，数字1已经不在窗口中了，但我们将它保存在堆中并不影响此时获得的最大值；
> 
> 所以我们只需要踢掉不在窗口中的最大值即可；
> 
> 只有在被踢元素恰好是当前堆中**最大值**的时候，我们才需要对堆进行调整；