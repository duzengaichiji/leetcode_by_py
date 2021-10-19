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