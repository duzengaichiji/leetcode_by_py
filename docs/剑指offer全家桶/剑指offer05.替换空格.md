剑指offer05.替换空格
----------
 - 题目
>请实现一个函数，把字符串 s 中的每个空格替换成"%20"。
 - 示例
 ----------
>input: s = "We are happy."

> output: "We%20are%20happy."
 ----------
 - 代码
 > 
> 
    class Solution:
        def replaceSpace(self, s: str) -> str:
            return "%20".join(s.split(" "))
 ----------
 - 解析
 > 解析个屁