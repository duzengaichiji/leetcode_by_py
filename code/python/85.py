class Solution:
    def calArea(self,heights_):
        res = 0
        heights = heights_.copy()
        heights.append(0)
        stack = []
        i = 0
        #利用单调栈，计算每个位置可以做成的最大的矩形
        while i<len(heights):
            if len(stack)==0 or heights[i]>heights[stack[-1]]:
                stack.append(i)
                i+=1
            else:
                cur = stack[-1]
                stack.pop()
                res = max(res,heights[cur]*(i if len(stack)==0 else i-stack[-1]-1))
        return res

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if len(matrix)==0:
            return 0
        res = 0
        heights = [0]*len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j]=='0':
                    heights[j] = 0
                else:
                    heights[j]+=1
            #到当前层为止，各个为止的最大高度
            print(heights)
            res = max(res,self.calArea(heights))
        return res