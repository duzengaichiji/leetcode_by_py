剑指offer58-1.翻转单词顺序
----------
 - 题目
>输入一个英文句子，翻转句子中单词的顺序，但单词内字符的顺序不变。为简单起见，标点符号和普通字母一样处理。例如输入字符串"I am a student. "，则输出"student. a am I"。去掉多余的空格

 - 示例
 ----------
>
 ----------
 - 代码
 >
>
    class Solution:
        def reverseWords(self, s: str) -> str:
            temp = s.split(' ')
            temp = [t.strip() if t.strip()!='' else "" for t in temp]
            temp_ = []
            for t in temp:
                if t!="":
                    temp_.append(t)
            return " ".join(temp_[::-1])
 ----------
 - 解析
> 