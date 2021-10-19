class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        heights.append(0)
        stack = []
        i = 0
        #维护一个单调递增栈
        while i<len(heights):
            if len(stack)==0 or heights[i]>heights[stack[-1]]:
                stack.append(i)
                i+=1
            #触发弹出条件，要计算当前最大的矩形大小
            else:
                cur = stack[-1]
                stack.pop()
                res = max(res,heights[cur]*(i if len(stack)==0 else i-stack[-1]-1))
        return res