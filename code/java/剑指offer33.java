class Solution {
    public boolean judege(int[] midorder,int[] postorder,int l_m,int r_m,int l_p,int r_p){
        if(l_m>r_m) return true;
        if(l_m==r_m) return midorder[l_m]==postorder[l_p];
        int root = postorder[r_p];
        int i = l_m;
        while(i<=r_m){
            if(midorder[i]==root) break;
            i+=1;
        }
        if(i>r_m) return false;
        boolean left = judege(midorder,postorder,l_m,i-1,l_p,l_p+(i-l_m)-1);
        boolean right = judege(midorder,postorder,i+1,r_m,l_p+(i-l_m),r_p-1);
        return left&right;
    }

    public boolean verifyPostorder(int[] postorder) {
        int[] midorder = new int[postorder.length];
        for(int i=0;i<midorder.length;i++) midorder[i]=postorder[i];
        Arrays.sort(midorder);
        return judege(midorder,postorder,0,midorder.length-1,0,midorder.length-1);
    }
}