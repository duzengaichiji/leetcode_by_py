剑指offer56-1.数组中数字出现的次数
----------
 - 题目
>一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。请写程序找出这两个只出现一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)。

 - 示例
 ----------
>input: [1,2,10,4,1,4,3,3]

> output: [2,10]
 ----------
 - 代码
 >
>
    class Solution:
        def singleNumbers(self, nums: List[int]) -> List[int]:
            ret = 0
            for num in nums:
                ret = num^ret
            div = 1
            while div&ret==0:
                div<<=1
            a,b = 0,0
            for num in nums:
                if num&div:
                    a^=num
                else:
                    b^=num
            return [a,b]
 ----------
 - 解析
 > 由只有一个不成对的数字那道题的启发，可以想到，仍然使用亦或来做；
>
> 本题的关键在于，如何分离数组中的那两个单独数字；
>
> 首先，假设这两个数字为x，y；
>
> 则整个数组的亦或，可以得到 x^y 的结果；
>
>
    ret = 0
    for num in nums:
        ret = num^ret
>
> 显然，ret不会为0，那么显而易见，ret的二进制表示中，值为1的位数上面；x和y在该位数上的值是不同的；
>
>
    div = 1
    while div&ret==0:
        div<<=1
>
> 上述代码将求得ret二进制表示中最 右边 的一个1； （假如为第3位，那么div=4，第二位,div=2...)
>
> 
    a,b = 0,0
    for num in nums:
        if num&div:
            a^=num
        else:
            b^=num
>
> 上述代码中，在div最高位为1的数字，被分配给a，否则分配给b;
>
> 由于除了x,y两个数字外，其他数字都是重复，所以都会被自己亦或给抵消掉；
>
> 因此 a,b 的最终结果就是x,y;
> 