/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode reverseList(ListNode head) {
        if(head==null||head.next==null) return head;
        ListNode pre = head;
        ListNode cur = head.next;
        ListNode newhead = null;
        while(cur!=null){
            pre.next = newhead;
            newhead = pre;
            pre = cur;
            cur = cur.next;
        }
        pre.next = newhead;
        newhead = pre;
        return newhead;
    }
}