class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        push_i = 0
        pop_i = 0

        while push_i<len(pushed) or pop_i<len(popped):
            if len(stack)==0 or stack[-1]!=popped[pop_i]:
                if push_i>=len(pushed):
                    return False
                stack.append(pushed[push_i])
                push_i+=1
            else:
                if stack:
                    stack.pop()
                    pop_i+=1
                else:
                    return False
        return True
