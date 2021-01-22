class Solution:
    def printNumbers(self, n: int) -> List[int]:
        res = [i+1 for i in range(int("".join(['9']*n)))]
        return res