剑指offer45.把数组排成最小的数
----------
 - 题目
>输入一个非负整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
> 
 - 示例
 ----------
> input: nums = [10，2]
> 
> output: "102"
 ----------
 - 代码
 >
> 方法一 
>
    class Solution:
        def minNumber(self, nums: List[int]) -> str:
            def sort(l,r):
                #print(nums)
                if l>=r:return
                i,j = l,r
                inc = nums[l]
                while i<j:
                    while i<j and compare(nums[j],inc,0,0)==True:
                        j-=1
                    if i<j:
                        nums[i] = nums[j]
                        i+=1
                    while i<j and compare(inc,nums[i],0,0)==True:
                        i+=1
                    if i<j:
                        nums[j] = nums[i]
                        j-=1
                nums[j] = inc
                if j-l>1:
                    sort(l,j-1)
                if r-j>1:
                    sort(j+1,r)
                return
            def compare(num1,num2,i1,i2):
                if num1==num2:
                    return True
                if len(set(num1))==1 and len(set(num2))==1 and num2[0]==num1[0]:
                    return True
                if num1[i1]<num2[i2]:
                    return False
                elif num1[i1]>num2[i2]:
                    return True
                else:
                    i1+=1
                    i1 = i1%len(num1)
                    i2+=1
                    i2 = i2%len(num2)
                    return compare(num1,num2,i1,i2)
            nums = [str(num) for num in nums]
            sort(0,len(nums)-1)
            return "".join(nums)
>
> 方法二
>
    class Solution:
        def minNumber(self, nums: List[int]) -> str:
            def fast_sort(l , r):
                if l >= r: return
                i, j = l, r
                while i < j:
                    while strs[j] + strs[l] >= strs[l] + strs[j] and i < j: j -= 1
                    while strs[i] + strs[l] <= strs[l] + strs[i] and i < j: i += 1
                    strs[i], strs[j] = strs[j], strs[i]
                strs[i], strs[l] = strs[l], strs[i]
                fast_sort(l, i - 1)
                fast_sort(i + 1, r)
            
            strs = [str(num) for num in nums]
            fast_sort(0, len(strs) - 1)
            return ''.join(strs)
  ----------
 - 解析
 > 简单来说，这个题目其实是在排序，按照数字对应的字符串“大小”进行排序，排序之后拼接即可得到答案；
>
> 如何定义字符串之间的大小是关键，因此要自己设计比较算法；
>
> 对于两个同样长度字符串的比较，分几种情况；
>
> 1.两个字符串相同，随意返回True 或者 False 都行，本题目没有相对位置的要求；
>
> 2.不等长情况；可以逐位比较；
>
> 假设 num1 = "123", num2 = "32"，那么显然，"32123"要比"12332"来得大；
>
> 但是如果 num1 = "123",num2 = "12"，这种情况，逐位比较到 num2的最后一位，仍然无法得到比较结果；
>
> 因此比较算法需要设计成递归形式；当某个串走到末位，则回到首位继续比较；
>
> 为什么是回到首位？ 上述例子中的两个组合串 "12**3**12"，“12**1**23"，当比较到num2的末位并递归回到第一位时，其实是在比较组合串中的第三位（因为num1的前几位和num2相同)
>
> 
    def compare(num1,num2,i1,i2):
        # 两串相同
        if num1==num2:
            return True
        # 特殊情况，例如"333" 和 "33"，这样会导致无限递归;
        if len(set(num1))==1 and len(set(num2))==1 and num2[0]==num1[0]:
            return True
        if num1[i1]<num2[i2]:
            return False
        elif num1[i1]>num2[i2]:
            return True
        else:
            # 相同，递归进行下一轮比较
            i1+=1
            i1 = i1%len(num1)
            i2+=1
            i2 = i2%len(num2)
            return compare(num1,num2,i1,i2)
>
> 当然，对于可以直接进行字符串比较的语言，有更简单的方法；
>
> 直接比较 num1+num2和num2+num1两个组合串的大小即可。。。
>