class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        return "".join([s[n:],s[:n]])