class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        # 已经记录过的点
        seen = {(0,0)}
        pq = [(grid[0][0],0,0)]
        ans = 0
        while pq:
            d,r,c = heapq.heappop(pq)
            ans = max(ans,d)
            # 可以抵达右下角
            if r==c==N-1: return ans
            for cr,cc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                if 0<=cr<N and 0<=cc<N and (cr,cc) not in seen:
                    heapq.heappush(pq,(grid[cr][cc],cr,cc))
                    seen.add((cr,cc))