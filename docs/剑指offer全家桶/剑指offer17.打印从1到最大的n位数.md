剑指offer17.打印从1到最大的n位数
----------
 - 题目
>输入数字 n，按顺序打印出从 1 到最大的 n 位十进制数。比如输入 3，则打印出 1、2、3 一直到最大的 3 位数 999。
 - 示例
 ----------
>input: 1

> output: [1,2,3,4,5,6,7,8,9]
 ----------
 - 代码
 >
>
    class Solution:
        def printNumbers(self, n: int) -> List[int]:
            res = [i+1 for i in range(int("".join(['9']*n)))]
            return res
  ----------
 - 解析
 > 