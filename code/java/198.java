class Solution {
    public int rob(int[] nums) {
        if(nums.length==0) return 0;
        if(nums.length==1) return nums[0];
        int[] stolen = new int[nums.length];
        int[] unstolen = new int[nums.length];
        stolen[0] = nums[0];
        unstolen[0] = 0;
        stolen[1] = nums[1];
        unstolen[1] = nums[0];
        for(int i=2;i<nums.length;i++){
            stolen[i] = unstolen[i-1]+nums[i];
            unstolen[i] = Math.max(stolen[i-1],unstolen[i-1]);
        }
        return Math.max(stolen[nums.length-1],unstolen[nums.length-1]);
    }
}