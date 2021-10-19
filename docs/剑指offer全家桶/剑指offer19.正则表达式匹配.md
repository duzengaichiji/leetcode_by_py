剑指offer19.正则表达式匹配
----------
 - 题目
>给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。

>    '.' 匹配任意单个字符
>    '*' 匹配零个或多个前面的那一个元素

>所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。

 - 示例
 ----------
 > input: s = "aa",p="a"
 >
 > output: false
 > 
> "a" 无法匹配"aa"整个字符串
>
> input: s = 'aa',p='a*'
>
> output: true
----------
- 代码
> 动态规划
>
    class Solution:
        def isMatch(self, s: str, p: str) -> bool:
            if not p: return not s
            if not s and len(p) == 1: return False 
    
            nrow = len(s) + 1
            ncol = len(p) + 1
    
            dp = [[False for c in range(ncol)] for r in range(nrow)]
            
            dp[0][0] = True
            dp[0][1] = False
            for c in range(2, ncol):
                j = c-1
                # 这里从dp[0][0]开始的话，是将*当作0个来用的
                if p[j] == '*': dp[0][c] = dp[0][c-2]
            
            for r in range(1, nrow):
                i = r-1
                for c in range(1, ncol):
                    j = c-1
                    if s[i] == p[j] or p[j] == '.':
                        dp[r][c] = dp[r-1][c-1]
                    elif p[j] == '*':
                        if p[j-1] == s[i] or p[j-1] == '.':
                            dp[r][c] = dp[r-1][c] or dp[r][c-2]
                        else:
                            dp[r][c] = dp[r][c-2]
                    else:
                        dp[r][c] = False
    
            return dp[nrow-1][ncol-1]
>
> 递归
>
    class Solution:
        def isMatch(self, s: str, p: str) -> bool:
            def match(si,pi):
                # 是否到字符串的末尾
                if pi==len(p):
                    return si==len(s)
                # 遇到带*的子串
                if pi<len(p)-1 and p[pi+1]=='*':
                    # *代表0个的情况；*代表n个的情况(n>=1)
                    return match(si,pi+2) or \
                        (si<len(s) and (s[si]==p[pi] or p[pi]=='.') and match(si+1,pi))
                else:
                    if si>=len(s):
                        return False
                    return (s[si]==p[pi] or p[pi]=='.') and match(si+1,pi+1)
            return match(0,0)
----------
- 解析
> 这个问题，应该和编辑距离联系起来；
>
> 我们姑且放着'*'号不管，只匹配字符和'.'号的话；
>
> 显然有 s[:i]和p[:j]的匹配，取决于 s[:i-1]和p[:j-1]的匹配结果，以及s[i]==p[j] or p[j]=='.'， 即取决于子结构；
>
> 
    if s[i] == p[j] or p[j] == '.':
        dp[r][c] = dp[r-1][c-1]
    else:
        dp[r][c] = False
>
> 如果考虑 * 号，则考虑需要子串 s[i:] 需要匹配'*'号前面的那个字符，要作为多少个（0-infinity）来使用；
>
> 已知p[j]=='*'，如果当作0个，s[i]应该等于 p[j-2]，因为 p[j-1]被当作0个，所以无需匹配p[j-1]；
>
> 如果当作1个以上，s[i]应该匹配 p[j-1]，因为至少 s[i]==p[j-1]，后面可能会有s[i+1]==p[j-1],s[i+2]==p[j-1]。。。
>
> 
    elif p[j] == '*':
        if p[j-1] == s[i] or p[j-1] == '.':
            dp[r][c] = dp[r-1][c] or dp[r][c-2]
        else:
            dp[r][c] = dp[r][c-2]