class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # 各种任务的计数
        freq = collections.Counter(tasks)
        m = len(freq)
        nextValid = [1]*m
        rest = list(freq.values())
        # 计算执行的总时长
        time = 0
        for i in range(len(tasks)):
            time+=1
            # 不在冷却且剩余时间最长的任务的下一次可执行时间
            minNextValid = min(nextValid[j] for j in range(m) if rest[j]>0)
            # 最早有效时间
            time = max(time,minNextValid)

            best = -1
            # 选取剩余次数最多的去执行
            for j in range(m):
                if rest[j] and nextValid[j]<=time:
                    if best==-1 or rest[j]>rest[best]:
                        best = j
            # 下一次启动该任务，需要等待n
            nextValid[best] = time + n + 1
            rest[best] -= 1

        return time