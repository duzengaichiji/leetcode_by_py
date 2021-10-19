/*
// Definition for a Node.
class Node {
    public int val;
    public Node left;
    public Node right;

    public Node() {}

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val,Node _left,Node _right) {
        val = _val;
        left = _left;
        right = _right;
    }
};
*/
class Solution {
    public Node treeToDoublyList(Node root) {
        if(root==null) return null;
        Stack<Node> stack = new Stack<>();
        List<Node> res = new ArrayList<>();
        Node cur = root;
        while(true){
            while(cur!=null){
                stack.push(cur);
                cur = cur.left;
            }
            if(!stack.isEmpty()) cur = stack.pop();
            else break;
            res.add(cur);
            if(cur.right!=null) cur = cur.right;
            else cur = null;
        }

        Node head = res.get(0);
        head.left = res.get(res.size()-1);
        Node pre = head;
        for(int i=1;i<res.size();i++){
            res.get(i).left = pre;
            pre.right = res.get(i);
            pre = res.get(i);
        }
        res.get(res.size()-1).right = head;
        return head;
    }
}