class Solution {

    public int mergeSort(int[] tmp,int[] nums,int left,int right){
        if(left>=right) return 0;

        int mid = (left+right)/2;
        int res = mergeSort(tmp,nums,left,mid)+mergeSort(tmp,nums,mid+1,right);

        int i = left;
        int j = mid+1;
        int index = left;
        while(i<=mid&&j<=right){
            if(nums[i]<=nums[j]){
                tmp[index++] = nums[i++];
                res+=(j-(mid+1));
            }
            else tmp[index++] = nums[j++];
        }
        while(i<=mid){
            tmp[index++] = nums[i++];
            res+=(j-(mid+1));
        }
        while(j<=right) tmp[index++] = nums[j++];
        for(int k=left;k<=right;k++) nums[k] = tmp[k];
        return res;
    }

    public int reversePairs(int[] nums) {
        int[] tmp = new int[nums.length];
        int res = mergeSort(tmp,nums,0,nums.length-1);
        return res;
    }
}