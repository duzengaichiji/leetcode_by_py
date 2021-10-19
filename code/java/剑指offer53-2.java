class Solution {
    public int missingNumber(int[] nums) {
        int l=0,r=nums.length-1;
        while(l<r){
            int mid = (l+r)/2;
            if(nums[mid]==mid) l = mid+1;
            else r = mid-1;
        }
        return nums[l]==l?l+1:l;
    }
}