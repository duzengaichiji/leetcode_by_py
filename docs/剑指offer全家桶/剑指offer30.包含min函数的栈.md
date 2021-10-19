剑指offer30.包含min函数的栈
----------
 - 题目
>定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，调用 min、push 及 pop 的时间复杂度都是 O(1)。
 - 示例
 ----------

 ----------
 - 代码
 >
>
    class MinStack:
    
        def __init__(self):
            """
            initialize your data structure here.
            """
            self.stack = []
            self.minstack = []
    
        def push(self, x: int) -> None:
            if not self.stack:
                self.stack.append(x)
                self.minstack.append(0)
            else:
                self.stack.append(x)
                if x<=self.stack[self.minstack[-1]]:
                    self.minstack.append(len(self.stack)-1)
    
        def pop(self) -> None:
            popd = self.stack[-1]
            if popd==self.stack[self.minstack[-1]]:
                self.minstack.pop()
            self.stack.pop()
            return popd
    
        def top(self) -> int:
            return self.stack[-1] if self.stack else -1
    
        def min(self) -> int:
            return self.stack[self.minstack[-1]] if self.minstack else -1
    
    
    # Your MinStack object will be instantiated and called as such:
    # obj = MinStack()
    # obj.push(x)
    # obj.pop()
    # param_3 = obj.top()
    # param_4 = obj.min()
  ----------
 - 解析
 > 
> 借助一个单调栈，保存递减的元素；
> 
>  单调栈的栈顶就是最小的元素；
> 
>  在弹出的时候注意弹出的是否是最小元素；如果是，则单调栈也要一同弹出来变更当前最小元素