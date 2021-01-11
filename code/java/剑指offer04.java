class Solution {
    public boolean findNumberIn2DArray(int[][] matrix, int target) {
        if(matrix==null||matrix.length==0) return false;
        int m = matrix.length;
        int n = matrix[0].length;
        int i = 0;
        int j = n-1;
        while(i>=0&&i<m&&j>=0&&j<n){
            if(matrix[i][j]>target) j--;
            else if(matrix[i][j]<target) i++;
            else if(matrix[i][j]==target) return true;
        }
        return false;
    }
}