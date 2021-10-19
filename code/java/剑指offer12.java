class Solution {
    public boolean backtrack(String word,char[][] board,int index,int length,int i,int j,int row,int col,boolean[][] used){
        if(index==length) return true;
        int[] d_r = {-1,1,0,0};
        int[] d_c = {0,0,-1,1};
        boolean res = false;
        for(int d=0;d<4;d++){
            if(i+d_r[d]>=0&&i+d_r[d]<row&&j+d_c[d]>=0&&j+d_c[d]<col){
                if(!used[i+d_r[d]][j+d_c[d]]&&word.charAt(index)==board[i+d_r[d]][j+d_c[d]]){
                    used[i+d_r[d]][j+d_c[d]] = true;
                    res = res|backtrack(word,board,index+1,length,i+d_r[d],j+d_c[d],row,col,used);
                    used[i+d_r[d]][j+d_c[d]] = false;
                }
            }
        }
        return res;
    }

    public boolean exist(char[][] board, String word) {
        int row = board.length;
        int col = board[0].length;
        int length = word.length();
        for(int i=0;i<row;i++){
            for(int j=0;j<col;j++){
                if(board[i][j]==word.charAt(0)){
                    boolean[][] used = new boolean[row][col];
                    used[i][j] = true;
                    if(backtrack(word,board,1,length,i,j,row,col,used)) return true;
                }
            }
        }
        return false;
    }
}