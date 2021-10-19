剑指offer31.栈的压入，弹出序列
----------
 - 题目
>输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否为该栈的弹出顺序。假设压入栈的所有数字均不相等。例如，序列 {1,2,3,4,5} 是某栈的压栈序列，序列 {4,5,3,2,1} 是该压栈序列对应的一个弹出序列，但 {4,3,5,1,2} 就不可能是该压栈序列的弹出序列。
 - 示例
 ----------
> input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
> 
> output: true
 ----------
 - 代码
 >
>
    class Solution:
        def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
            stack = []
            push_i = 0  
            pop_i = 0
    
            while push_i<len(pushed) or pop_i<len(popped):
                # 当前栈空，或者没到要pop的位置
                if len(stack)==0 or stack[-1]!=popped[pop_i]:
                    # 如果栈顶不等于当前要pop的值，且已经没有元素可以push，则卒
                    if push_i>=len(pushed):
                        return False
                    stack.append(pushed[push_i])
                    push_i+=1
                else:
                    # 碰到要弹出的元素时，若没有元素可以弹出，则卒
                    if stack:
                        stack.pop()
                        pop_i+=1
                    else:
                        return False
            return True

    
  ----------
 - 解析
 > 
> 直接模拟栈的压入，弹出过程，碰到不合理的位置就返回False;