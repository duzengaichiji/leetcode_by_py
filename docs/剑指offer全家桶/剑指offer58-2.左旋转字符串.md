剑指offer58-2.左旋转字符串
----------
 - 题目
>字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。请定义一个函数实现字符串左旋转操作的功能。比如，输入字符串"abcdefg"和数字2，该函数将返回左旋转两位得到的结果"cdefgab"。


 - 示例
 ----------
>input: s = "abcdefg", k = 2

> output: "cdefgab"
 ----------
 - 代码
 >
>
    class Solution:
        def reverseLeftWords(self, s: str, n: int) -> str:
            return "".join([s[n:],s[:n]])
 ----------
 - 解析
> 