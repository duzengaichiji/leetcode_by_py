class Solution {
    public int majorityElement(int[] nums) {
        Map<Integer,Integer> counter = new HashMap<>();
        int count;
        int half = nums.length>>1;
        for(int i=0;i<nums.length;i++){
            if(counter.containsKey(nums[i])){
                count = counter.get(nums[i]);
                count+=1;
                if(count>half){
                    return nums[i];
                }
                counter.remove(nums[i]);
                counter.put(nums[i],count);
            }else{
                if(1>half) return nums[i];
                counter.put(nums[i],1);
            }
        }
        return -1;
    }
}