剑指offer14-1.剪绳子
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
            if n<=3:return n-1
            a,b = n//3,n%3
            if b==0:return int(math.pow(3,a))
            if b==1:return int(math.pow(3,a-1)*4)
            return int(math.pow(3,a)*2)
  ----------
 - 解析
 > 数学题，不解释；