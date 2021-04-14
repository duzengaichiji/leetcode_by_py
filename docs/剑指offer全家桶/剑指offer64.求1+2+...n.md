剑指offer64.求1+2+。。。n
----------
 - 题目
>求 1+2+...+n ，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。

 - 示例
 ----------
>input: n = 3

> output: 6
 ----------
 - 代码
 >
>
    class Solution:
        def sumNums(self, n: int) -> int:
            return n*(n+1)//2
 ----------
 - 解析
 >
> 等差数列前n项目和。。