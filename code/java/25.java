/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode reverse(ListNode head){
        ListNode p = head;
        ListNode q = head.next;
        if(q==null)
            return head;
        head = q;
        p.next = null;
        while(head!=null){
            head = head.next;
            q.next = p;
            p = q;
            q = head;
        }
        return p;
    }

    public ListNode reverseKGroup(ListNode head, int k) {
        ListNode result = null;
        int count = 1;
        ListNode start = head;
        ListNode end = null;
        ListNode last = null;
        while(head!=null){
            if(count==k){
                end = head;
                head = head.next;
                end.next = null;
                end = reverse(start);
                if(result==null)
                    result = end;
                if(last==null){
                    last = start;
                }
                else{
                    last.next = end;
                    last = start;
                }
                start = head;
                count = 1;
            }
            else{
                count++;
                head = head.next;
            }
        }
        if(count>1){
            if(last==null)
                return start;
            last.next = start;
        }
        return result;
    }
}