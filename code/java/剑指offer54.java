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
    public int kthLargest(TreeNode root, int k) {
        List<Integer> res = new ArrayList<>();
        Stack<TreeNode> stack = new Stack<>();
        while(true){
            while(root!=null){
                stack.push(root);
                root = root.left;
            }
            if(stack.isEmpty()) break;
            root = stack.pop();
            res.add(root.val);
            if(root.right!=null){
                root = root.right;
            }else{
                root = null;
            }
        }
        //System.out.print(res);
        return res.get(res.size()-k);
    }
}