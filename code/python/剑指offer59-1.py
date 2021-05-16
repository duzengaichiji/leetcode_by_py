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