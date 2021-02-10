class Solution {
    public int maxSubArray(int[] nums) {
        int temp = nums[0];
        int res = nums[0];
        for(int i=1;i<nums.length;i++){
            temp = Math.max(temp+nums[i],nums[i]);
            res = Math.max(temp,res);
        }
        return res;
    }
}