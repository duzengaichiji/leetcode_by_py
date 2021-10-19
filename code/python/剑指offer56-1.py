class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        ret = 0
        for num in nums:
            ret = num^ret
        div = 1
        print(ret)
        while div&ret==0:
            div<<=1
        print(div)
        a,b = 0,0
        for num in nums:
            if num&div:
                a^=num
            else:
                b^=num
        return [a,b]