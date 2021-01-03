class Solution:
    def fib(self, n: int) -> int:
        if n<=1:
            return n
        if n==2:
            return 1
        a = 0
        b = 1
        for i in range(2,n+1):
            temp = b
            b = (b+a)%(1e9+7)
            a = temp
        #print(a,b)
        return int(b)