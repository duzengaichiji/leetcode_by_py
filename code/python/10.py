class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        #备忘录记录已经搜索过的地方
        memo = dict()
        def dp(i,j):
            #已经搜索过的结果，直接返回
            if (i,j) in memo:return memo[(i,j)]
            if j>=len(p):
                return i>=len(s)
            first_match = i<len(s) and p[j] in {s[i],'.'}
            if j<=len(p)-2 and p[j+1]=='*':
                res = dp(i,j+2) or (first_match and dp(i+1,j))
            else:
                res = first_match and dp(i+1,j+1)
            memo[(i,j)] = res
            return res
        return dp(0,0)