class Solution:
    def dicesProbability(self, n: int) -> List[float]:
        pre = [1/6]*6
        for i in range(2,n+1):
            tmp = [0]*(5*i+1)
            for j in range(len(pre)):
                for x in range(6):
                    tmp[j+x] += pre[j]/6
            pre = tmp
        return pre