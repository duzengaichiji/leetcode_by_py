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