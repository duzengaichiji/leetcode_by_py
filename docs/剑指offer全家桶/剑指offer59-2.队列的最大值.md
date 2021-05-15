剑指offer59-2.队列的最大值
----------
 - 题目
>请定义一个队列并实现函数 max_value 得到队列里的最大值，要求函数max_value、push_back 和 pop_front 的均摊时间复杂度都是O(1)。
>
>若队列为空，pop_front 和 max_value 需要返回 -1
>
 - 示例
 ----------
> input:["MaxQueue","push_back","push_back","max_value","pop_front","max_value"] [[],[1],[2],[],[],[]]
> 
> output: [null,null,null,2,1,2]
 ----------
 - 代码
 >
>
    import queue
    class MaxQueue:
    
        def __init__(self):
            self.queue = queue.Queue()
            self.deque = queue.deque()
    
        def max_value(self) -> int:
            return self.deque[0] if self.deque else -1
    
        def push_back(self, value: int) -> None:
            self.queue.put(value)
            while self.deque and self.deque[-1] < value:
                self.deque.pop()
            self.deque.append(value)
    
        def pop_front(self) -> int:
            if self.queue.empty(): return -1
            val = self.queue.get()
            if val == self.deque[0]:
                self.deque.popleft()
            return val
    
    
    # Your MaxQueue object will be instantiated and called as such:
    # obj = MaxQueue()
    # param_1 = obj.max_value()
    # obj.push_back(value)
    # param_3 = obj.pop_front()
  ----------
 - 解析
 > 
> 关键在于保证能直接取到队列中的最大值；
>
> 因此考虑用一个**单调**双向队列，保存当前队列中的【最大值，次大值。。。】
>
> 1.为什么用双向？
>
> 2.怎么保证不丢失最大值，每次都能取到？