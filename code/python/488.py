class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        maxInt = float('inf')
        m = len(hand)
        # str:int
        # 记录某个串消到最后所需要的次数
        mem = {}

        def dfs(b, cur):
            if len(b) == 0: return 0
            # 该串已经记录过了
            if b in mem: return mem[b]
            ans = maxInt
            n = len(b)
            # 尝试手中所有的球
            for i in range(m):
                # 已经使用过的球就跳过，然后指向下一个
                if (cur >> i) & 1 == 1: continue
                nextPos = (1 << i) | cur
                # 尝试board上的n+1个位置
                for j in range(n + 1):
                    sb = []
                    # 插入手中的球
                    sb.extend(list(b[:j]))
                    sb.append(hand[i])
                    # 插入位置不是尾部的话，需要加入后半段
                    if j != n: sb.extend((b[j:]))
                    k = j
                    # 检查插入位置两端的相同字符长度
                    while k >= 0 and k < len(sb):
                        c = sb[k]
                        l = k
                        r = k
                        while l >= 0 and sb[l] == c: l -= 1
                        while r < len(sb) and sb[r] == c: r += 1
                        # 满足消除条件
                        if r - l - 1 >= 3:
                            # 消除掉满足条件的部分
                            sb = sb[:l + 1] + sb[r:]
                            # 消除后要重新检测满足条件的子串
                            k = l if l >= 0 else r
                        else:
                            break
                    ans = min(ans, dfs("".join(sb), nextPos) + 1)
            mem[b] = ans
            return ans

        res = dfs(board, 1 << m)
        return res if res != maxInt else -1