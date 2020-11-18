class Solution {
    public int minimumDeleteSum(String s1, String s2) {
        int length1 = s1.length();
        int length2 = s2.length();
        int[][] dp = new int[length1+1][length2+1];

        for(int i=length1-1;i>=0;i--) dp[i][length2] = dp[i+1][length2]+s1.charAt(i)-'a'+97;
        for(int i=length2-1;i>=0;i--) dp[length1][i] = dp[length1][i+1]+s2.charAt(i)-'a'+97;

        for(int i=length1-1;i>=0;i--){
            for(int j=length2-1;j>=0;j--){
                if(s1.charAt(i)==s2.charAt(j)){
                    dp[i][j] = dp[i+1][j+1];
                }else{
                    dp[i][j] = Math.min(
                        dp[i+1][j]+s1.charAt(i)-'a'+97,
                        dp[i][j+1]+s2.charAt(j)-'a'+97
                    );
                }
            }
        }
        return dp[0][0];
    }
}