剑指offer13.机器人的运动范围
----------
 - 题目
>地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？

----------
 - 示例
> input:m = 2, n = 3, k = 1
>
> output:3
 ----------
 - 代码
 >
> BFS
>
>
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
>
>
>DFS
>
>
    class Solution:
        def movingCount(self, m: int, n: int, k: int) -> int:
            def backtrack(r,c,used):
                if r<0 or r>=m or c<0 or c>=n:
                    return
                number = 0
                r_ = r
                c_ = c
                if used[r][c]==1:
                    return
                while r_>0:
                    number+=r_%10
                    r_ = r_//10
                while c_>0:
                    number+=c_%10
                    c_ = c_//10
                if number>k:
                    return
                used[r][c] = 1
                backtrack(r+1,c,used)
                backtrack(r-1,c,used)
                backtrack(r,c+1,used)
                backtrack(r,c-1,used)
                return
            used = [[0]*n for _ in range(m)]
            backtrack(0,0,used)
            return sum([sum(row) for row in used])
 ----------
 - 解析
 > bfs或者dfs都可以，过滤掉不可达的点，以及因为这些点而导致的不可达点即可