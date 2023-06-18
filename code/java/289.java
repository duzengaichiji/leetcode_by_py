class Solution {
    public int checkBox(int[][] board,int i,int j,int m,int n){
        int result = 0;
        if(i>0&&j>0)
            result+=board[i-1][j-1]>0?1:0;
        if(i>0)
            result+=board[i-1][j]>0?1:0;
        if(i>0&&j<n-1)
            result+=board[i-1][j+1]>0?1:0;
        if(j>0)
            result+=board[i][j-1]>0?1:0;
        if(j<n-1)
            result+=board[i][j+1]>0?1:0;
        if(i<m-1&&j>0)
            result+=board[i+1][j-1]>0?1:0;
        if(i<m-1)
            result+=board[i+1][j]>0?1:0;
        if(i<m-1&&j<n-1)
            result+=board[i+1][j+1]>0?1:0;
        return result;
    }

    public void gameOfLife(int[][] board) {
        int m = board.length;
        int n = board[0].length;
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                int temp = checkBox(board,i,j,m,n);
                if(board[i][j]==0)
                    board[i][j] = -1*temp;
                else{
                    if(temp==0)
                        temp = 1;
                    board[i][j] = temp;
                }
            }
        }
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                if(board[i][j]!=-3&&board[i][j]!=2&&board[i][j]!=3)
                    board[i][j]=0;
                else
                    board[i][j]=1;
            }
        }
    }
}