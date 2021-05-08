class Solution {
    public boolean isStraight(int[] nums) {
        int[] result = new int[14];
        for(int num:nums) result[num]+=1;
        int left = -1;
        int right = -1;
        for(int i=1;i<=13;i++){
            if(result[i]>0){
                left = i;
                break;
            }
        }
        for(int i=13;i>=1;i--){
            if(result[i]>0){
                right = i;
                break;
            }
        }
        if(left==right) return true;
        for(int i=left;i<=right;i++){
            if(result[i]>1) return false;
            else if(result[i]==0){
                if(result[0]>0) result[0]-=1;
                else return false;
            }
        }
        return true;
    }
}