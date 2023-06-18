class Solution:
    def reverse(self, x: int) -> int:
        signal = 1 if x>=0 else -1
        nums = str(x)
        if x<0: nums = nums[1:]
        nums = nums[::-1]
        num = int(nums)
        if -2**31<=num<=2**31-1:
            return signal*num
        else:
            return 0