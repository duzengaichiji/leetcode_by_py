/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public boolean isSub(TreeNode a,TreeNode b){
        if((a==null&&b!=null)||(a!=null&&b==null)) return false;
        if(a.val!=b.val) return false;
        boolean leftRes = true;
        if(b.left!=null) leftRes = isSub(a.left,b.left);
        boolean rightRes = true;
        if(b.right!=null) rightRes = isSub(a.right,b.right);
        return leftRes&&rightRes;
    }

    public boolean judge(TreeNode a,TreeNode b){
        if(a==null) return false;
        if(isSub(a,b)) return true;
        else return judge(a.left,b)|judge(a.right,b);
    }

    public boolean isSubStructure(TreeNode A, TreeNode B) {
        if(B==null) return false;
        return judge(A,B);
    }
}