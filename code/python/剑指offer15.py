class Solution:
    def hammingWeight(self, n: int) -> int:
        return collections.Counter(bin(n))['1']