剑指offer48.最长不含重复字符的子字符串
----------
 - 题目
>请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。
>
 - 示例
 ----------
> input: "abcabcbb"
> 
> output: 3
 ----------
 - 代码
 >
>
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
  ----------
 - 解析
 > 
> 双指针；
>
> 保证两个指针之间的子串没有重复字符，这样就可以遍历所有的 没有重复字符的子串；
>
> 因此，在每次遇到子串中包含重复字符时，将前指针后移，直至不包含重复字符为止；
>
>
    # 发现重复字符
    while True and i<j:
        # 找到与s[j]一致的重复字符
        if s[i]==s[j]:
            # 将该字符的计数-1，（在该题中只有1和0）
            curMap[s[j]]-=1
            break
        # s[i]不是重复字符的情况下，将i后移继续找，不过要将s[i]的计数-1；
        curMap[s[i]]-=1
        i+=1
    # 找到重复字符之后也要将该字符跳过
    i+=1