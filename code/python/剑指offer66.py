class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        if not a:return []
        pre = [a[0]]
        for num in a[1:-1]:
            pre.append(pre[-1]*num)
        order = [a[-1]]
        for num in a[::-1][1:-1]:
            order.append(order[-1]*num)
        order = order[::-1]
        print(pre,order)
        res = []
        for i in range(len(a)):
            if i==0:
                res.append(order[0])
            elif i==len(a)-1:
                res.append(pre[-1])
            else:
                res.append(pre[i-1]*order[i])
        return res