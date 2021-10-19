class Solution {
    public List<List<Integer>> fourSum(int[] nums, int target) {
        if(nums.length<4) return new ArrayList<>();
        List<List<Integer>> res = new ArrayList<>();
        Arrays.sort(nums);
        int length = nums.length;

        for(int i=0;i<length-3;i++){
            if(i>0&&nums[i]==nums[i-1]) continue;
            if(nums[i]+nums[i+1]+nums[i+2]+nums[i+3]>target) break;
            if(nums[i]+nums[length-1]+nums[length-2]+nums[length-3]<target) continue;
            for(int j=i+1;j<length-2;j++){
                if(j>i+1&&nums[j]==nums[j-1]) continue;
                if(nums[i]+nums[j]+nums[j+1]+nums[j+1]>target) break;
                if(nums[i]+nums[j]+nums[length-1]+nums[length-2]<target) continue;
                int l = j+1;
                int r = length-1;
                while(l<r){
                    int sum = nums[i]+nums[j]+nums[l]+nums[r];
                    if(sum==target){
                        res.add(Arrays.asList(nums[i],nums[j],nums[l],nums[r]));
                        while(l<r&&nums[l]==nums[l+1]) l++;
                        while(l<r&&nums[r]==nums[r-1]) r--;
                        l++;
                        r--;
                    }else if(sum<target) l++;
                    else r--;
                }
            }
        }
        return res;
    }
}