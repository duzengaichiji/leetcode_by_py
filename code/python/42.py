class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height)<3:
            return 0
        stack = []
        stack.append(0)
        res = 0
        i = 1
        #for i in range(len(height)):
        while i<len(height):
            if len(stack)==0 or height[i]<height[stack[-1]]:
                stack.append(i)
                i+=1
            elif height[i]>=height[stack[-1]]:
                last = 0
                while len(stack)>0 and height[stack[-1]]<=height[i]:
                    #print(last)
                    left = stack.pop()
                    res+=(height[left]-last)*(i-left-1)
                    last = height[left]
                stack.append(i)
                if len(stack)>1:
                    #print(stack,i)
                    res+=(height[i]-last)*(i-stack[-2]-1)
                i+=1
        return res