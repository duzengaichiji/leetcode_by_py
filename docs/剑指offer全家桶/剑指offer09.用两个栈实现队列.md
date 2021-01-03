剑指offer09.用两个栈实现队列
----------
 - 题目
>用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，deleteHead 操作返回 -1 )

来源：力扣（LeetCode）
----------
 - 示例
> input :["CQueue","appendTail","deleteHead","deleteHead"] [[],[3],[],[]]
>
> output: [null,null,3,-1]
 ----------
 - 代码
 >
>
    
    class CQueue:
    
        def __init__(self):
            self.stack1 = []
            self.stack2 = []
    
        def appendTail(self, value: int) -> None:
            self.stack1.append(value)
    
        def deleteHead(self) -> int:
            #print(self.stack1,self.stack2)
            if not self.stack1 and not self.stack2:
                return -1
            elif self.stack2:
                return self.stack2.pop()
            elif self.stack1 and not self.stack2:
                while self.stack1:
                    self.stack2.append(self.stack1.pop())
                return self.stack2.pop()
 ----------
 - 解析
 >
> 由于栈是先进后出，队列是先进先出；
>
> 所以需要两个栈，将整体顺序变为先进先出；
>
> 道理很简单，填充的时候先填充到第一个栈；
>
> 然后弹出的时候，若第二个栈非空，直接从第二个栈中弹出；
>
> 若第二个栈为空，则先将第一个栈中的所有元素弹出，并依次压入第二个栈，保证顺序是正确的，然后弹出即可；
>