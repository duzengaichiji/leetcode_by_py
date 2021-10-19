class Solution {
    public int[] fastSort(int[] nums,int start,int end){
        int inc = 0;
        if(start<end)
            inc = nums[start];
        else
            return nums;
        int left = start;
        int right = end;
        while(left<right){
            while(left<right&&nums[right]>=inc){
                right--;
            }
            if(left<right&&nums[right]<inc){
                nums[left] = nums[right];
                left++;
            }
            while(left<right&&nums[left]<=inc)
                left++;
            if(left<right&&nums[left]>inc){
                nums[right] = nums[left];
                right--;
            }
        }
        nums[right] = inc;
        if(right>start)
            fastSort(nums,start,right-1);
        if(right<end)
            fastSort(nums,right+1,end);
        return nums;
    }

    public int twoSumClosest(int[] nums,int start,int end,int target,int drop_index){
        int result = 0;
        int gap = 9999;
        while(start<end){
            if(start==drop_index){
                start++;
                continue;
            }
            if(end==drop_index){
                end--;
                continue;
            }
            if(nums[start]+nums[end]==target){
                result = nums[start]+nums[end];
                break;
            }
            if(nums[start]+nums[end]>target){
                if(Math.abs(target-(nums[start]+nums[end]))<gap){
                    gap = Math.abs(target-nums[start]-nums[end]);
                    result = nums[start]+nums[end];
                }
                end--;
                continue;
            }
            if(nums[start]+nums[end]<target){
                if(Math.abs(target-(nums[start]+nums[end]))<gap){
                    gap = Math.abs(target-nums[start]-nums[end]);
                    result = nums[start]+nums[end];
                }
                start++;
                continue;
            }
        }
        return result;
    }

    public int threeSumClosest(int[] nums, int target) {
        if(nums.length==3)
            return nums[0]+nums[1]+nums[2];
        //step 1.sort the array
        nums = fastSort(nums,0,nums.length-1);
        int cloest = 9999;
        int result = 0;

        for(int i=0;i<nums.length;i++){
            result = twoSumClosest(nums,0,nums.length-1,target-nums[i],i);
            if(Math.abs(target-(result+nums[i]))<Math.abs(target-cloest))
                cloest = result+nums[i];
        }

        return cloest;
    }
}