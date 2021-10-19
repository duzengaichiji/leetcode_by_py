class Solution {
    public int maxProfitForkDeals(int k,int[] prices){
        //需要多一次来表示初始状态
        int[] dp_i_0 = new int[k+1];
        int[] dp_i_1 = new int[k+1];
        for(int i=0;i<=k;i++) dp_i_1[i] = -Integer.MAX_VALUE;
        for(int price:prices){
            for(int i=1;i<=k;i++){
                dp_i_0[i] = Math.max(dp_i_0[i],dp_i_1[i]+price);
                dp_i_1[i] = Math.max(dp_i_1[i],dp_i_0[i-1]-price);
            }
        }
        return dp_i_0[k];
    }

    public int maxProfitForInfinityDeals(int[] prices){
        int dp_i_0 = 0;
        int dp_i_1 = -Integer.MAX_VALUE;
        int temp = -1;
        for(int price:prices){
            temp = dp_i_0;
            dp_i_0 = Math.max(dp_i_0,dp_i_1+price);
            dp_i_1 = Math.max(dp_i_1,temp-price);
        }
        return dp_i_0;
    }

    public int maxProfit(int k, int[] prices) {
        int length = prices.length;
        if(k>length/2) return maxProfitForInfinityDeals(prices);
        else return maxProfitForkDeals(k,prices);
    }
}