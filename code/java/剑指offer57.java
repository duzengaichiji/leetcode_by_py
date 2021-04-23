class Solution {
    public int[] twoSum(int[] nums, int target) {
        Arrays.sort(nums);
        int i=0,j=nums.length-1;
        while(nums[i]+nums[j]!=target){
            if(nums[i]+nums[j]>target) j--;
            else i++;
        }
        return new int[]{nums[i],nums[j]};
    }
}