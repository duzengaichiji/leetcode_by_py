class Solution:
    def __init__(self):
        self.index = 0

    def scanUnsignedInteger(self,s):
        before = self.index
        while self.index<len(s) and s[self.index]>='0' and s[self.index]<='9':
            self.index+=1
        return self.index>before

    def scanInteger(self,s):
        if self.index<len(s) and (s[self.index]=='-' or s[self.index]=='+'):
            self.index+=1
        return self.scanUnsignedInteger(s)

    def isNumber(self, s: str) -> bool:
        if s is None or len(s)==0: return False
        while self.index<len(s) and s[self.index]==' ':
            self.index+=1
        numeric = self.scanInteger(s)
        if self.index<len(s) and s[self.index]=='.':
            self.index+=1
            numeric = self.scanUnsignedInteger(s) or numeric
        if self.index<len(s) and (s[self.index]=='E' or s[self.index]=='e'):
            self.index+=1
            numeric = numeric and self.scanInteger(s)
        while self.index<len(s) and s[self.index]==' ':
            self.index+=1
        return numeric and self.index==len(s)