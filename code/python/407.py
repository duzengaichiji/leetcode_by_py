class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        # 少于三行或三列的是没法接水的
        if len(heightMap) <= 2 or len(heightMap[0]) <= 2:
            return 0
        m, n = len(heightMap), len(heightMap[0])
        visited = [[0 for _ in range(n)] for _ in range(m)]
        pq = []
        # 外墙壁先入队
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    visited[i][j] = 1
                    heapq.heappush(pq, (heightMap[i][j], i * n + j))

        res = 0
        dirs = [-1, 0, 1, 0, -1]
        while pq:
            # 弹出当前最矮的柱子
            height, position = heapq.heappop(pq)
            # 遍历四个方向
            for k in range(4):
                nx, ny = position // n + dirs[k], position % n + dirs[k + 1]
                if nx >= 0 and nx < m and ny >= 0 and ny < n and visited[nx][ny] == 0:
                    if height > heightMap[nx][ny]:
                        res += height - heightMap[nx][ny]
                    visited[nx][ny] = 1
                    heapq.heappush(pq, (max(height, heightMap[nx][ny]), nx * n + ny))
        return res