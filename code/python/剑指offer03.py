class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        count = collections.Counter(nums)
        for key,value in count.items():
            if value>1:
                return key
        return 0