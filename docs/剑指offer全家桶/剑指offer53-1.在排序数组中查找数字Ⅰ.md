剑指offer53-1.在排序数组中查找数字Ⅰ
----------
 - 题目
>统计一个数字在排序数组中出现的次数。
>
 - 示例
 ----------
> input: nums = [5,7,7,8,8,10], target = 8
> 
> output: 2
 ----------
 - 代码
 >
>
    class Solution:
        def search(self, nums: List[int], target: int) -> int:
            if not nums: return 0
            l = 0
            r = len(nums)-1
            while l<=r:
                mid = (l+r)//2
                if nums[mid]<target:
                    l = mid+1
                elif nums[mid]>target:
                    r = mid-1
                else:
                    break
            if l>r: return 0
            l = mid
            r = mid
            while l>=0 and nums[l]==nums[mid]: l-=1
            while r<len(nums) and nums[r]==nums[mid]: r+=1
            return r-l-1
  ----------
 - 解析
 > 
> 用二分查找找到目标数字，然后根据找到的位置向两边扩散，找到所有目标数字即可；
>