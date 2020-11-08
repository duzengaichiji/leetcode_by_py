class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        def recursive(cum, lower, upper, left, right):
            if left == right:
                return 0, cum
            # 归并左右两边
            mid = (left + right) // 2
            n1, cum = recursive(cum, lower, upper, left, mid)
            n2, cum = recursive(cum, lower, upper, mid + 1, right)
            res = n1 + n2
            # 统计下标对的数量
            i = left
            l = mid + 1
            r = mid + 1
            # 由于两个数组（两边）都是升序的，所以一轮遍历即可得到下标对数
            while i <= mid:
                while l <= right and cum[l] - cum[i] < lower:
                    l += 1
                while r <= right and cum[r] - cum[i] <= upper:
                    r += 1
                res += (r - l)
                i += 1
            # 归并排序
            newCum = cum.copy()
            index = left
            p1 = left
            p2 = mid + 1
            while p1 <= mid and p2 <= right:
                if cum[p1] <= cum[p2]:
                    newCum[index] = cum[p1]
                    p1 += 1
                    index += 1
                else:
                    newCum[index] = cum[p2]
                    p2 += 1
                    index += 1
            while p1 <= mid:
                newCum[index] = cum[p1]
                p1 += 1
                index += 1
            while p2 <= right:
                newCum[index] = cum[p2]
                p2 += 1
                index += 1
            return res, newCum

        # 求取前缀和数组
        if not nums:
            return 0
        cum = [0]
        for num in nums:
            cum.append(cum[-1] + num)
        result, cum = recursive(cum, lower, upper, 0, len(cum) - 1)
        return result