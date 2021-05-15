class Solution {
    public int search(int[] nums, int target) {
        int l = 0,r = nums.length-1;
        if(r==-1) return 0;
        int mid = -1;
        while(l<=r){
            mid = (l+r)/2;
            if(nums[mid]<target) l = mid+1;
            else if(nums[mid]>target) r = mid-1;
            else break;
        }
        if(l>r) return 0;
        l = mid;
        r = mid;
        while(l>=0&&nums[l]==nums[mid]) l--;
        while(r<nums.length&&nums[r]==nums[mid]) r++;
        return r-l-1;
    }
}