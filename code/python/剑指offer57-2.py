class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        l = 1
        r = 2
        res = []
        while l < r:
            s = (l + r) * (r - l + 1) / 2
            if s == target:
                res.append([i for i in range(l, r + 1)])
                l += 1
            elif s > target:
                l += 1
            else:
                r += 1
        return res