class Solution {
    public void setZeroes(int[][] matrix) {
        int m = matrix.length;
        int n = matrix[0].length;
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                if(matrix[i][j]==0){
                    for(int k1=0;k1<n;k1++){
                        if(matrix[i][k1]!=999&&matrix[i][k1]!=0)
                            matrix[i][k1]=999;
                    }
                    for(int k2=0;k2<m;k2++){
                        if(matrix[k2][j]!=999&&matrix[k2][j]!=0)
                            matrix[k2][j]=999;
                    }
                }
            }
        }
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                if(matrix[i][j]==999)
                    matrix[i][j]=0;
            }
        }
    }
}