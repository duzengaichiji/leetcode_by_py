class Solution {
    public int maxProfit(int[] prices) {
        int dp_i_0 = 0;
        int dp_i_1 = Integer.MIN_VALUE;
        int dp_i_0_0 = 0;
        int temp = 0;
        for(int i=0;i<prices.length;i++){
            dp_i_0_0 =temp;
            temp = dp_i_0;
            dp_i_0 = Math.max(dp_i_0,dp_i_1+prices[i]);
            dp_i_1 = Math.max(dp_i_1,dp_i_0_0-prices[i]);
        }
        return dp_i_0;
    }
}