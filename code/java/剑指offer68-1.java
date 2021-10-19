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
    private TreeNode ans = null;

    public TreeNode dfs(TreeNode node,TreeNode p,TreeNode q){
        if(node==null) return null;
        if(node==p||node==q){
            if(dfs(node.left,p,q)!=null||dfs(node.right,p,q)!=null) ans=ans==null?node:ans;
            return node;
        }
        TreeNode getl = dfs(node.left,p,q);
        TreeNode getr = dfs(node.right,p,q);
        if(getl!=null&&getr!=null){
            ans=ans==null?node:ans;
            return node;
        }else if(getl!=null||getr!=null){
            return node;
        }else{
            return null;
        }
    }

    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        dfs(root,p,q);
        return ans;
    }
}