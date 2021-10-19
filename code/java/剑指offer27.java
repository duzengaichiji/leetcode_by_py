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
    public TreeNode reverse(TreeNode node){
        if(node==null) return node;
        node.left = reverse(node.left);
        node.right = reverse(node.right);
        TreeNode temp = node.left;
        node.left = node.right;
        node.right = temp;
        return node;
    }
    public TreeNode mirrorTree(TreeNode root) {
        root = reverse(root);
        return root;
    }
}