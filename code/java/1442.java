class Solution {
    public int countTriplets(int[] arr) {
        if(arr.length==0) return 0;
        int[] res = new int[arr.length+1];
        for(int i=0;i<arr.length;i++){
            res[i+1] = res[i]^arr[i];
        }
        int c = 0;
        for(int i=0;i<arr.length;i++){
            for(int j=i+1;j<arr.length;j++){
                if(res[i]==res[j+1]) c+=(j-i);
            }
        }
        return c;
    }
}