class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        if not nums or len(nums)<4: return []
        nums = sorted(nums)
        length = len(nums)

        for i in range(length-3):
            # 重复数字，跳过
            if i>0 and nums[i]==nums[i-1]:
                continue
            if nums[i]+nums[i+1]+nums[i+2]+nums[i+3]>target:
                break
            # 该数一定找不到对应组合
            if nums[i]+nums[length-3]+nums[length-2]+nums[length-1]<target:
                continue
            for j in range(i+1,length-2):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                # 后面的组合一定会超过target
                if nums[i]+nums[j]+nums[j+1]+nums[j+1]>target:
                    break
                if nums[i]+nums[j]+nums[length-2]+nums[length-1]<target:
                    continue
                left,right = j+1,length-1
                while left<right:
                    total = nums[i]+nums[j]+nums[left]+nums[right]
                    if total==target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        while left<right and nums[left]==nums[left+1]:
                            left+=1
                        left+=1
                        while left<right and nums[right]==nums[right-1]:
                            right-=1
                        right-=1
                    elif total>target:
                        right-=1
                    else:
                        left+=1
        return res