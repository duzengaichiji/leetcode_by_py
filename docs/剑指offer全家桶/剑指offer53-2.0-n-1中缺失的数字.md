剑指offer53-2.0-n-1中缺失的数字
----------
 - 题目
>一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0～n-1之内。在范围0～n-1内的n个数字中有且只有一个数字不在该数组中，请找出这个数字。
>
 - 示例
 ----------
> input:[0,1,3]
> 
> output: 2
 ----------
 - 代码
 >
>
    class Solution:
        def missingNumber(self, nums: List[int]) -> int:
            l,r = 0,len(nums)-1
            while l<r:
                mid = (l+r)//2
                if nums[mid]==mid:
                    l = mid+1
                else:
                    r = mid-1
            if nums[l]==l:
                return l+1
            else:
                return l
  ----------
 - 解析
 > 
> 由于数组是按照[0-n-1]递增排列，且仅抠去了一个数字；
>
> 因此采用二分查找，当 nums[x]==x 的时候，说明 x前面的数字是满足 nums[i]=i 的对应关系；
>
> 因此被抠去的数字只在x位置后面，只需要查找后面的数字；
>
> 最后当 l==r 时会退出循环；
>
> 此时仍然需要检查是否满足nums[i]==i的条件；