class Solution {
    public int robMax(int[] nums,int start,int end){
        int dp_i_0 = 0; // 偷
        int dp_i_1 = 0; // 不偷
        int dp_i = 0;
        for(int i=start;i<end;i++){
            dp_i = dp_i_1;
            dp_i_1 = Math.max(dp_i_0,dp_i_1);
            dp_i_0 = dp_i+nums[i];
        }
        return Math.max(dp_i_0,dp_i_1);
    }

    public int rob(int[] nums) {
        if(nums.length==0) return 0;
        if(nums.length==1) return nums[0];
        if(nums.length==2) return Math.max(nums[0],nums[1]);
        int n = nums.length;
        return Math.max(robMax(nums,0,n-1),robMax(nums,1,n));
    }
}