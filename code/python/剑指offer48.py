class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        curMap = {}
        i = 0
        j = 0
        while j<len(s):
            c = s[j]
            if c not in curMap or curMap[c]==0:
                curMap[c] = 1
                res = max(res,j-i+1)
                j+=1
            else:
                while True and i<j:
                    if s[i]==s[j]:
                        curMap[s[j]]-=1
                        break
                    curMap[s[i]]-=1
                    i+=1
                i+=1
        res = max(res,j-i)
        return res