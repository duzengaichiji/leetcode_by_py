剑指offer57-2.和为s的连续正数序列
----------
 - 题目
>输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。
>
>序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。

 - 示例
 ----------
>target = 9

> output: [[2,3,4],[4,5]]
 ----------
 - 代码
 >
>
    class Solution:
        def findContinuousSequence(self, target: int) -> List[List[int]]:
            l = 1
            r = 2
            res = []
            while l<r:
                s = (l+r)*(r-l+1)/2
                if s==target: 
                    res.append([i for i in range(l,r+1)])
                    l+=1
                elif s>target:
                    l+=1
                else:
                    r+=1
            return res
 ----------
 - 解析
> 
>
> 连续正数和可以求得；
>
    s = (l+r)*(r-l+1)/2
>
> 因此，使用双指针向前移动；
> 
> 每当和值比目标值大时候，缩小[l,r]的范围，因此，l前移；反之，增大[l,r]的范围，将r前移；
>
> 当r移动到target附近时，总是会有[l,r]范围内的数字和>target，此时l不断前移，直至和r相遇，就停止；