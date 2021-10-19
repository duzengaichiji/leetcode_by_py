/*
// Definition for a Node.
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}
*/
class Solution {
    public Node copyRandomList(Node head) {
        if(head==null) return null;
        Map<Node,Node> map = new HashMap<>();
        Node temp = head;
        Node last = null;
        while(temp!=null){
            Node node = new Node(temp.val);
            if(last==null) last = node;
            else{
                last.next = node;
                last = node;
            }
            map.put(temp,node);
            temp = temp.next;
        }
        temp = head;
        while(temp!=null){
            if(temp.random==null){
                map.get(temp).random=null;
            }else{
                map.get(temp).random = map.get(temp.random);
            }
            temp =temp.next;
        }
        return map.get(head);
    }
}