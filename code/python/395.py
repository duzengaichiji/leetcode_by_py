class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        def get(c): return ord(c)-ord('a')

        def helper(s):
            n,h = len(s),[0]*26

            for i in range(n): h[get(s[i])]+=1
            f = False
            for i,v in enumerate(h):
                if v!=0 and v<k:
                    f = True
            if not f:return n

            st,res = 0,0
            for e in range(n):
                if h[get(s[e])]<k:
                    res = max(res,helper(s[st:e]))
                    st = e+1
                elif e==n-1:
                    res = max(res,helper(s[st:e+1]))

            return res
        return helper(s)