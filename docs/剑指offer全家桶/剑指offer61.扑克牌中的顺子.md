剑指offer61.扑克牌中的顺子
----------
 - 题目
>从扑克牌中随机抽5张牌，判断是不是一个顺子，即这5张牌是不是连续的。2～10为数字本身，A为1，J为11，Q为12，K为13，而大、小王为 0 ，可以看成任意数字。A 不能视为 14。

 - 示例
 ----------
>input: [0,0,1,2,5]

> output: True
 ----------
 - 代码
 >
>
    class Solution:
        def isStraight(self, nums: List[int]) -> bool:
            result = [0]*14
            for num in nums:
                result[num]+=1
            left = -1
            right = -1
            for i in range(1,14):
                if result[i]>0:
                    left = i
                    break
            for i in range(13,0,-1):
                if result[i]>0:
                    right = i
                    break
            # 如果最大的牌=最小的牌 or 根本没有牌
            if left==right:
                return True
    
            for i in range(left,right+1):
                if result[i]>1:
                    return False
                elif result[i]==0:
                    if result[0]>0:
                        result[0]-=1
                    else:
                        return False
            return True
 ----------
 - 解析
 >
> 先用一个数组记录每张牌的数量；
>
> 然后找到最大的牌以及最小的牌；
>
> 然后按照规则，如果有重复的牌，就卒；
>
> 否则看看能不能用0号牌来替代不连续的区间；