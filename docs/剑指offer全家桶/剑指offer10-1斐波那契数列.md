剑指offer10-1.斐波那契数列
----------
 - 题目
>写一个函数，输入 n ，求斐波那契（Fibonacci）数列的第 n 项。斐波那契数列的定义如下：

> F(0) = 0,   F(1) = 1
>
>F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
> 斐波那契数列由 0 和 1 开始，之后的斐波那契数就是由之前的两数相加而得出。
>
> 答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。
>
----------
 - 示例

>
 ----------
 - 代码
 >
>
    class Solution:
        def fib(self, n: int) -> int:
            if n<=1:
                return n
            if n==2:
                return 1
            a = 0
            b = 1
            for i in range(2,n+1):
                temp = b
                b = (b+a)%(1e9+7)
                a = temp
            #print(a,b)
            return int(b)
 ----------
 - 解析
 >
> 