class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        qindex = list(range(len(queries)))
        qindex.sort(key=lambda i: queries[i])
        intervals.sort(key=lambda i: i[0])
        pq = []
        res = [-1] * len(queries)
        i = 0
        for qi in qindex:
            # 满足当前查询条件的区间，都要放到堆里面
            while i < len(intervals) and intervals[i][0] <= queries[qi]:
                heappush(pq, (intervals[i][1] - intervals[i][0] + 1, intervals[i][0], intervals[i][1]))
                i += 1
            # 踢出不满足本轮查询的区间，剩余的堆定就是满足条件的最小区间
            while pq and pq[0][2] < queries[qi]:
                heappop(pq)
            if pq:
                res[qi] = pq[0][0]
        return res