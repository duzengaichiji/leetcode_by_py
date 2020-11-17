class Solution {
    int max=Integer.MAX_VALUE;
     public int coinChange(int[] coins, int amount) {
         int[] dp = new int[amount+1];
         for(int i=1;i<=amount;i++) dp[i] = max;
         for(int coin:coins){
             for(int i=coin;i<=amount;i++){
                 dp[i] = Math.min(dp[i],dp[i-coin]+1);
             }
         }
         if(dp[amount]==max) return -1;
         else return dp[amount];
    }
}