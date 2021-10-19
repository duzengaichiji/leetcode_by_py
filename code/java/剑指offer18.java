/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode deleteNode(ListNode head, int val) {
        if(head.val == val) return head.next;
        ListNode pre = head;
        ListNode node = head;
        while(node!=null){
            if(node.val==val) break;
            pre = node;
            node = node.next;
        }
        pre.next = node.next;
        node.next = null;
        return head;
    }
}