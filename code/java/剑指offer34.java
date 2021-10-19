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
    List<List<Integer>> res;

    public void dfs(TreeNode root,List<Integer> path,int value,int sum){
        path.add(root.val);
        value+=root.val;
        if(value==sum){
            if(root.left==null&&root.right==null) res.add(new ArrayList<>(path));
        }
        if(root.left!=null) dfs(root.left,path,value,sum);
        if(root.right!=null) dfs(root.right,path,value,sum);
        value-=root.val;
        path.remove(path.size()-1);
    }

    public List<List<Integer>> pathSum(TreeNode root, int sum) {
        if(root==null) return new ArrayList<>(0);
        res = new ArrayList<>();
        List<Integer> path = new ArrayList<>();
        dfs(root,path,0,sum);
        return res;
    }
}