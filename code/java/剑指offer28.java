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
    public boolean sCompare(TreeNode node1,TreeNode node2){
        if(node1==null&&node2==null) return true;
        if(node1!=null&&node2==null) return false;
        if(node1==null&&node2!=null) return false;
        if(node1.val!=node2.val) return false;
        return sCompare(node1.left,node2.right)&&sCompare(node1.right,node2.left);
    }

    public boolean isSymmetric(TreeNode root) {
        return sCompare(root,root);
    }
}