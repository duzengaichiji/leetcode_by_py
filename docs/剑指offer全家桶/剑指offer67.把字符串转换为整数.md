剑指offer67.把字符串转换为整数
----------
 - 题目
>给定一个数组 A[0,1,…,n-1]，请构建一个数组 B[0,1,…,n-1]，其中 B[i] 的值是数组 A 中除了下标 i 以外的元素的积, 即 B[i]=A[0]×A[1]×…×A[i-1]×A[i+1]×…×A[n-1]。不能使用除法。

 - 示例
 ----------
>input: "-91283472332"

> output: -2147483648
 ----------
 - 代码
 >
>
    class Solution:
        def strToInt(self, string: str) -> int:
            # 截断前部空白
            s = list(string)
            i = 0
            while i<len(s) and s[i]==' ': i+=1
            if i==len(s): return 0
    
            s = s[i:]
    
            nums = ["1","2","3","4","5","6","7","8","9","0"]
            if s[0]!='+' and s[0]!='-' and s[0] not in nums:
                return 0
            
            signal = 1
            if s[0]=='+': s = s[1:]
            elif s[0]=='-':
                signal = -1
                s = s[1:]
            
            i = 0
            while i<len(s) and s[i] in nums: i+=1
            s = s[:i]
            if not s:return 0
            if signal==-1:
                s.insert(0,'-')
                s = "".join(s)
                res = int(s)
                if res<-2147483648:
                    return -2147483648
            else:
                s = "".join(s)
                res = int(s)
                if res>2147483647:
                    return 2147483647
            return res
            

 ----------
 - 解析
 > 
> 没啥说的。。按照规则写就行了