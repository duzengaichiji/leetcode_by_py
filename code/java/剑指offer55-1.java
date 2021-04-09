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
    public int maxDepth(TreeNode root) {
        if(root==null) return 0;
        int deep = 1;
        List<TreeNode> q = new ArrayList<>();
        q.add(root);
        TreeNode last = root;
        while(q.size()>0){
            TreeNode cur = q.get(0);
            q.remove(0);
            if(cur.left!=null) q.add(cur.left);
            if(cur.right!=null) q.add(cur.right);
            if(last==cur){
                if(q.size()>0){
                    last = q.get(q.size()-1);
                    deep++;
                }
            }
        }
        return deep;
    }
}