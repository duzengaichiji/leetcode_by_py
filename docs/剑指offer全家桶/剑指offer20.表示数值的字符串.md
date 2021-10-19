剑指offer20.表示数值的字符串
----------
 - 题目
>请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。例如，字符串"+100"、"5e2"、"-123"、"3.1416"、"-1E-16"、"0123"都表示数值，但"12e"、"1a3.14"、"1.2.3"、"+-5"及"12e+5.4"都不是。
 - 示例
 ----------

 ----------
 - 代码
 >
>
    class Solution:
        def __init__(self):
            self.index = 0
    
        def scanUnsignedInteger(self,s):
            before = self.index
            # 判断是否数字
            while self.index<len(s) and s[self.index]>='0' and s[self.index]<='9':
                self.index+=1
            # 只有后面才有字符才可以继续（java解中补充了结束符号）
            # 如果碰到非数字，则下一部分的判断会出错
            return self.index>before
    
        def scanInteger(self,s):
            # 跳过符号
            if self.index<len(s) and (s[self.index]=='-' or s[self.index]=='+'):
                self.index+=1
            # 判断
            return self.scanUnsignedInteger(s)
    
        def isNumber(self, s: str) -> bool:
            if s is None or len(s)==0: return False
            # 跳过开头的空白
            while self.index<len(s) and s[self.index]==' ':
                self.index+=1
            # 
            numeric = self.scanInteger(s)
            # 跳过小数点
            if self.index<len(s) and s[self.index]=='.':
                self.index+=1
                # 判断小数部分是否数字
                numeric = self.scanUnsignedInteger(s) or numeric
            # 判断'e'部分是否是数字
            if self.index<len(s) and (s[self.index]=='E' or s[self.index]=='e'):
                self.index+=1
                numeric = numeric and self.scanInteger(s)
            while self.index<len(s) and s[self.index]==' ':
                self.index+=1
            return numeric and self.index==len(s)
  ----------
 - 解析
 > 
> 
>  将一个数字分为三个部分， A.BeC；
> 
>  即整数部分，小数部分，'e'后面的部分；
> 
>  