/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode rotateRight(ListNode head, int k) {
        if(head==null)
            return null;
        ListNode result;
        int len = 0;
        ListNode s = head;
        while(s!=null){
            len++;
            s = s.next;
        }
        k = k%len;
        if(k==0)
            return head;
        else{
            int stop = len-k;
            int i = 1;
            s = head;
            while(i<stop){
                s = s.next;
                i++;
            }
            result = s.next;
            s.next = null;
            s = result;
            while(s.next!=null)
                s = s.next;
            s.next = head;
            return result;
        }
    }
}