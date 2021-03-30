class Solution:
    def firstUniqChar(self, s: str) -> str:
        count = Counter(list(s))
        for char in s:
            if count[char]==1:
                return char
        return " "