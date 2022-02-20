class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {num:index for index,num in enumerate(nums)}
        res = []
        for i,num in enumerate(nums):
            if target-num in hashMap and i!=hashMap[target-num]:
                return [i,hashMap[target-num]]
        return res