class Solution {
    public int maxProfit(int[] prices) {
        int K = 2;

        int[] dp_0 = new int[K+1];
        int[] dp_1 = new int[K+1];
        for(int i=0;i<=K;i++) dp_1[i] = Integer.MIN_VALUE;
        for(int i=0;i<prices.length;i++){
            for(int k=1;k<=K;k++){
                int temp = dp_0[k];
                dp_0[k] = Math.max(dp_0[k],dp_1[k]+prices[i]);
                dp_1[k] = Math.max(dp_1[k],dp_0[k-1]-prices[i]);
            }
        }
        return dp_0[K];
    }
}