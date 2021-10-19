class Solution {
    public int maximumGap(int[] nums) {
        int length = nums.length;
        if(length<=1) return 0;
        int minVal = Integer.MAX_VALUE;
        int maxVal = Integer.MIN_VALUE;
        for(int num:nums){
            if(num<minVal) minVal = num;
            if(num>maxVal) maxVal = num;
        }
        // 所有数字都一样
        if(maxVal==minVal) return 0;

        int interval = 0;
        // 间隔向上取整，保证length-1个桶可以包围[minVal,maxVal]这个范围
        if((float)(maxVal-minVal)/(length-1)>(maxVal-minVal)/(length-1)) interval = (maxVal-minVal)/(length-1)+1;
        else interval = (maxVal-minVal)/(length-1);

        int[] bucketMin = new int[length-1];
        int[] bucketMax = new int[length-1];
        for(int i=0;i<length-1;i++){
            bucketMax[i] = Integer.MIN_VALUE;
            bucketMin[i] = Integer.MAX_VALUE;
        }

        for(int num:nums){
            int index = (num-minVal)/interval;
            if(num==maxVal||num==minVal) continue;
            bucketMax[index] = Math.max(bucketMax[index],num);
            bucketMin[index] = Math.min(bucketMin[index],num);
        }

        int res = 0;
        int previous = minVal;
        for(int i=0;i<length-1;i++){
            if(bucketMax[i]==Integer.MIN_VALUE) continue;
            res = Math.max(bucketMin[i]-previous,res);
            previous = bucketMax[i];
        }
        res = Math.max(maxVal-previous,res);
        return res;
    }
}