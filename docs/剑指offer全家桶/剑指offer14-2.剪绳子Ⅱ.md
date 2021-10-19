剑指offer14-2.剪绳子Ⅱ
----------
 - 题目
>给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），每段绳子的长度记为 k[0],k[1]...k[m-1] 。请问 k[0]*k[1]*...*k[m-1] 可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。
>
 - 示例
 ----------
>input: 10

> output: 36 
 ----------
 - 代码
 >
>
    class Solution:
        def cuttingRope(self, n: int) -> int:
            if n <= 3: return n - 1
            a, b, p, x, rem = n // 3 - 1, n % 3, 1000000007, 3 , 1
            while a > 0:
                if a % 2: rem = (rem * x) % p
                x = x ** 2 % p
                a //= 2
            if b == 0: return (rem * 3) % p # = 3^(a+1) % p
            if b == 1: return (rem * 4) % p # = 3^a * 4 % p
            return (rem * 6) % p # = 3^(a+1) * 2  % p
  ----------
 - 解析
 > 数学题，不解释；