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
        def myPow(self, x: float, n: int) -> float:
            def pow(x,n):
                if n==0:
                    return 1
                if n==1:
                    return x
                if n%2==0:
                    return pow(x*x,n//2)
                if n%2!=0:
                    return x*pow(x*x,n//2)
    
            res = pow(x,abs(n))
            if n<0:
                return 1/res
            return res
  ----------
 - 解析
 > 