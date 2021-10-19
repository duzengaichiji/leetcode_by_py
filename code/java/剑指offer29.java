class Solution {
    public int[] spiralOrder(int[][] matrix) {
        if(matrix.length==0) return new int[0];
        int l = 0,r = matrix[0].length-1,t=0,b = matrix.length-1;
        int[] res = new int[(r+1)*(b+1)];
        int index = 0;
        while(true){
            for(int i=l;i<r+1;i++) res[index++] = matrix[t][i];
            t+=1;
            if(t>b) break;
            for(int i=t;i<b+1;i++) res[index++] = matrix[i][r];
            r-=1;
            if(l>r) break;
            for(int i=r;i>=l;i--) res[index++] = matrix[b][i];
            b-=1;
            if(t>b) break;
            for(int i=b;i>=t;i--) res[index++] = matrix[i][l];
            l+=1;
            if(l>r) break;
        }
        return res;
    }
}