/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Codec {

    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        if(root==null) return "[]";
        Queue<TreeNode> queue = new LinkedList<>();
        StringBuilder res = new StringBuilder("[");
        queue.offer(root);
        while(queue.size()>0){
            TreeNode cur = queue.remove();
            if(cur!=null){
                res.append(cur.val + ",");
                queue.offer(cur.left);
                queue.offer(cur.right);
            }else{
                res.append("null,");
            }
        }
        res.deleteCharAt(res.length() - 1);
        res.append("]");
        return res.toString();
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        if(data.equals("[]")) return null;
        String[] values = data.substring(1,data.length()-1).split(",");
        TreeNode root = new TreeNode(Integer.parseInt(values[0]));
        Queue<TreeNode> queue = new LinkedList<>();
        queue.add(root);
        int i = 1;
        while(queue.size()>0){
            TreeNode node = queue.remove();
            if(!values[i].equals("null")){
                node.left = new TreeNode(Integer.parseInt(values[i]));
                queue.add(node.left);
            }
            i+=1;
            if(!values[i].equals("null")){
                node.right = new TreeNode(Integer.parseInt(values[i]));
                queue.add(node.right);
            }
            i+=1;
        }
        return root;
    }
}

// Your Codec object will be instantiated and called as such:
// Codec codec = new Codec();
// codec.deserialize(codec.serialize(root));