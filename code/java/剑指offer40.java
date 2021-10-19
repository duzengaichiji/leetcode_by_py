class Solution {
    public int[] getLeastNumbers(int[] arr, int k) {
        int[] res = new int[k];
        Arrays.sort(arr);
        for(int i=0;i<k;i++) res[i] = arr[i];
        return res;
    }
}