剑指offer16.数值的整数次方
----------
 - 题目
>实现函数double Power(double base, int exponent)，求base的exponent次方。不得使用库函数，同时不需要考虑大数问题。
 - 示例
 ----------
>input: 2.00000, 10

> output: 1024.00000 
 ----------
 - 代码
 >
>
    class Solution:
        def hammingWeight(self, n: int) -> int:
            return collections.Counter(bin(n))['1']
  ----------
 - 解析
 > 