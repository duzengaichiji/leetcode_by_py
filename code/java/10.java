class Solution {
    public boolean isMatch(String s, String p) {
        int row = s.length();
        int col = p.length();
        boolean[][] dp =new boolean[row+1][col+1];

        dp[0][0] = true;
        for(int i=2;i<=col;i++){
            if(p.charAt(i-1)=='*') dp[0][i] = dp[0][i-2];
        }

        for(int i=1;i<=row;i++){
            int r = i-1;
            for(int j=1;j<=col;j++){
                int c = j-1;
                if(p.charAt(c)=='*'){
                    if(p.charAt(c-1)==s.charAt(r)||p.charAt(c-1)=='.')
                        dp[i][j] = dp[i-1][j]||dp[i][j-2];
                    else
                        dp[i][j] = dp[i][j-2];
                }else{
                    if(p.charAt(c)=='.'||s.charAt(r)==p.charAt(c)) dp[i][j] = dp[i-1][j-1];
                    else dp[i][j] = false;
                }
            }
        }
        return dp[row][col];
    }
}