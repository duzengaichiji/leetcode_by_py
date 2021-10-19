class Solution {
    public int[] exchange(int[] nums) {
        if(nums.length==0) return nums;
        int inc = nums[0];
        int start = 0;
        int end = nums.length-1;
        while(start<end){
            while(start<end&&nums[end]%2==0){
                end-=1;
            }
            if(start<end){
                nums[start] = nums[end];
                start+=1;
            }
            while(start<end&&nums[start]%2!=0){
                start+=1;
            }
            if(start<end){
                nums[end] = nums[start];
                end-=1;
            }
        }
        nums[end] = inc;
        return nums;
    }
}