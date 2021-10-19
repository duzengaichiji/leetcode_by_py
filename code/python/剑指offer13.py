class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        def judge(row,col,k):
            a = row//10
            a_ = row%10
            b = col//10
            b_ = col%10
            if a+a_+b+b_>k:
                return False
            return True
        used = [[False]*n for _ in range(m)]
        stack = [(0,0)]
        while len(stack)>0:
            cur = stack.pop()
            used[cur[0]][cur[1]] = True
            if cur[0]>0 and used[cur[0]-1][cur[1]]==False and judge(cur[0]-1,cur[1],k)==True:
                stack.append((cur[0]-1,cur[1]))
            if cur[0]<m-1 and used[cur[0]+1][cur[1]]==False and judge(cur[0]+1,cur[1],k)==True:
                stack.append((cur[0]+1,cur[1]))
            if cur[1]>0 and used[cur[0]][cur[1]-1]==False and judge(cur[0],cur[1]-1,k)==True:
                stack.append((cur[0],cur[1]-1))
            if cur[1]<n-1 and used[cur[0]][cur[1]+1]==False and judge(cur[0],cur[1]+1,k)==True:
                stack.append((cur[0],cur[1]+1))
        # for i in range(m):
        #     print(used[i])
        return sum([sum(used[i]) for i in range(m)])