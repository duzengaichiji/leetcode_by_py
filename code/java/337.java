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
    public int[] robTree(TreeNode root){
        if(root==null) return new int[]{0,0};
        int[] left = robTree(root.left);
        int[] right = robTree(root.right);
        int res = left[1]+right[1]+root.val;
        int resNon = Math.max(left[0],left[1])+Math.max(right[0],right[1]);
        return new int[]{res,resNon};
    }

    public int rob(TreeNode root) {
        int[] res = robTree(root);
        return Math.max(res[0],res[1]);
    }
}