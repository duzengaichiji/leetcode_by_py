剑指offer44.数字序列中某一位的数字
----------
 - 题目
>数字以0123456789101112131415…的格式序列化到一个字符序列中。在这个序列中，第5位（从下标0开始计数）是5，第13位是1，第19位是4，等等。
>
>请写一个函数，求任意第n位对应的数字。
> 
 - 示例
 ----------
> input: n = 3
> 
> output: 3
 ----------
 - 代码
 >
>
    class Solution:
        def findNthDigit(self, n: int) -> int:
            if n<10:
                return n
            digit,start,count = 1,1,9
            while n>count:
                n-=count
                start*=10
                digit+=1
                count = 9*start*digit
            num = start+(n-1)//digit
            s = str(num)
            res = int(s[(n-1)%digit])
            return res
  ----------
 - 解析
 > 
> 脑筋急转弯，跳过不解释