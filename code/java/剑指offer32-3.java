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
    public List<List<Integer>> levelOrder(TreeNode root) {
        Queue<TreeNode> queue = new LinkedList<>();
        List<List<Integer>> res = new ArrayList<>();
        if(root!=null) queue.offer(root);
        int turn = 1;
        while(queue.size()>0){
            List<Integer> tmp = new ArrayList<>();
            for(int i=queue.size();i>0;i--){
                TreeNode node = queue.remove();
                tmp.add(node.val);
                if(node.left!=null) queue.offer(node.left);
                if(node.right!=null) queue.offer(node.right);
            }
            if(turn==1){
                res.add(tmp);
            }else{
                List<Integer> temp = new ArrayList<>();
                for(int i=tmp.size()-1;i>=0;i--){
                    temp.add(tmp.get(i));
                }
                res.add(temp);
            }
            turn = 1-turn;
        }
        return res;
    }
}