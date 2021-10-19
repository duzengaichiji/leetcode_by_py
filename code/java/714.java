class Solution {
    public int maxProfit(int[] prices, int fee) {
        int dp_i_0 = 0;
        int dp_i_1 = -Integer.MAX_VALUE;
        int temp = -1;
        for(int price:prices){
            temp = dp_i_0;
            dp_i_0 = Math.max(dp_i_0,dp_i_1+price);
            dp_i_1 = Math.max(dp_i_1,temp-price-fee);
        }
        return dp_i_0;
    }
}