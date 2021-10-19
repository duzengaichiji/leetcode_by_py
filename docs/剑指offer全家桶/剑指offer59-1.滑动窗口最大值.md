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
 >
>
    import queue
    class Solution:
        def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
            deque = queue.deque()
            res = []
            for i in range(k):
                num = nums[i]
                while deque and deque[-1]<num:
                    deque.pop()
                deque.append(num)
            if deque: res.append(deque[0])
            for i in range(k,len(nums)):
                num = nums[i]
                out = nums[i-k]
                if out==deque[0]:
                    deque.popleft()
                while deque and deque[-1]<num:
                    deque.pop()
                deque.append(num)
                res.append(deque[0])
            return res
    
 ----------
 - 解析
 > 很大程度上参考 59-2 的解；