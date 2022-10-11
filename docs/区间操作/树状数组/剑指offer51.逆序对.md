剑指offer51.逆序对
----------
- 题目
> 在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。
> 
----------
- 示例
> input = [7,5,6,4]
> output = 5
----------
- 代码
>
    class TreeArr:
        def __init__(self,n):
            self.n = n
            self.tree = [0]*(n+1)
        def lowbit(self,x):
            return x&-x
        def query(self,x):
            ans = 0
            i = x
            while i>0:
                ans+=self.tree[i]
                i-=self.lowbit(i)
            return ans
        def add(self,x,d):
            i = x
            while i<=self.n:
                self.tree[i]+=d
                i+=self.lowbit(i)
    
    class Solution:
        def reversePairs(self, nums: List[int]) -> int:
            nums = sorted([(i,x) for i,x in enumerate(nums)],key = lambda x:x[1])
            n = len(nums)
            pos = [0]*n
            for i in range(n):
                pos[nums[i][0]] = i
    
            res = 0
            BIT = TreeArr(n)
            for i in range(n):
                left = pos[i]
                right = n-1
                # >nums[i]的数在树状数组中年存在的个数，即对nums[i]形成的逆序对
                res+=(BIT.query(right+1)-BIT.query(left))
                BIT.add(pos[i]+1,1)
            return res
----------
 - 解析
 > 参考493的解法，用树状数组寻找逆序对；
>