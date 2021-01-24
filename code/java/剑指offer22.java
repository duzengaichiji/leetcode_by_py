/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode getKthFromEnd(ListNode head, int k) {
        ListNode node = head;
        int i = 1;
        while(node.next!=null&&i<k){
            node = node.next;
            i+=1;
        }
        if(i<k){
            return null;
        }
        ListNode target = head;
        while(node.next!=null){
            node = node.next;
            target = target.next;
        }
        return target;
    }
}