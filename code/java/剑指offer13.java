class Solution {
    public boolean judge(int a,int b,int k){
        int a_1 = a/10;
        int a_0 = a%10;
        int b_1 = b/10;
        int b_0 = b%10;
        if(a_1+a_0+b_1+b_0>k) return false;
        return true;
    }

    public int movingCount(int m, int n, int k) {
        Stack<Integer> stack = new Stack<>();
        int[][] used = new int[m][n];
        //起点
        stack.push(0);
        while(!stack.isEmpty()){
            int cur = stack.pop();
            int row = cur/n;
            int col = cur%n;
            used[row][col] = 1;
            if(row>0&&(used[row-1][col]==0&&judge(row-1,col,k)))stack.push((row-1)*n+col);
            if(row<m-1&&(used[row+1][col]==0&&judge(row+1,col,k))) stack.push((row+1)*n+col);
            if(col>0&&(used[row][col-1]==0&&judge(row,col-1,k))) stack.push((row)*n+col-1);
            if(col<n-1&&(used[row][col+1]==0&&judge(row,col+1,k))) stack.push((row)*n+col+1);
        }

        int res = 0;
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                res+=used[i][j];
            }
        }
        return res;
    }
}