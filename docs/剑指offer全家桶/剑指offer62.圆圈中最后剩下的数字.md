剑指offer62.圆圈中最后剩下的数字
----------
 - 题目
>0,1,···,n-1这n个数字排成一个圆圈，从数字0开始，每次从这个圆圈里删除第m个数字（删除后从下一个数字开始计数）。求出这个圆圈里剩下的最后一个数字。
>
> 例如，0、1、2、3、4这5个数字组成一个圆圈，从数字0开始每次删除第3个数字，则删除的前4个数字依次是2、0、4、1，因此最后剩下的数字是3。

 - 示例
 ----------
>input: n = 5, m = 3

> output:  3
 ----------
 - 代码
 >
>
    # Python 默认的递归深度不够，需要手动设置
    sys.setrecursionlimit(100000)
    
    def f(n, m):
        if n == 0:
            return 0
        x = f(n - 1, m)
        return (m + x) % n
    
    class Solution:
        def lastRemaining(self, n: int, m: int) -> int:
            return f(n, m)
 ----------
 - 解析
 >
> #TODO