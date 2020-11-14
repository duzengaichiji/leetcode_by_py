class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = nums[0]
        count = 1
        # 选举
        for i in range(1,len(nums)):
            if nums[i]==candidate:
                count+=1
            else:
                if count==0:
                    candidate = nums[i]
                    count = 1
                else:
                    count-=1
        count = 0
        # 验证
        for num in nums:
            if num==candidate:
                count+=1
        if count>len(nums)//2:
            return candidate