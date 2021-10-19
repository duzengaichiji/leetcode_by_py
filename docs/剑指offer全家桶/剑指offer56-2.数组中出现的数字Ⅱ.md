剑指offer56-2.数组中数字出现的次数Ⅱ
----------
 - 题目
>在一个数组 nums 中除一个数字只出现一次之外，其他数字都出现了三次。请找出那个只出现一次的数字。

 - 示例
 ----------
>input: [9,1,7,9,7,9,7]

> output: 1
 ----------
 - 代码
 >
>
    class Solution:
        def singleNumber(self, nums: List[int]) -> int:
            counts = [0]*32
            for num in nums:
                for j in range(32):
                    counts[j]+=num&1
                    num>>=1
            res,m = 0,3
            for i in range(32):
                res<<=1
                res|=counts[31-i]%m
            return res

 ----------
 - 解析
 > 
> 该方法容易拓展到“只有一个数字出现一次，其他都出现 任意次 ” 的问题上，但是时间效率上，实际还不如直接用Counter统计。。
> 
> 由于只有一个数字出现一次，其他都出现了3次，因此除了那个单独数字的二进制位以外，其他所有的二进制位置，**要不是0个1，要不就是3个1**；
>
> 因此，利用一个32位数组来统计32个二进制位中1的个数
>
    counts = [0]*32
    for num in nums:
        # 统计num的所有二进制位
        for j in range(32):
            counts[j]+=num&1
            num>>=1
>
> 之后，将counts数组复原为数字即可，counts[i]%3即可得到当前二进制位上是1还是0，因此，counts代表着 **那个单独数字的所有二进制位**
>
    res,m = 0,3
    for i in range(32):
        # 左移，去匹配更高位
        res<<=1
        res|=counts[31-i]%m
>
> 
>