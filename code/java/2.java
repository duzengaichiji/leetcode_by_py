/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        if(l1==null) return l2;
        if(l2==null) return l1;
        ListNode res = l1;
        ListNode last = l1;
        ListNode pre_1 = null;
        ListNode pre_2 = null;
        int temp = 0;
        int inc = 0;
        while(l1!=null&&l2!=null){
            temp = l1.val+l2.val+inc;
            inc = temp/10;
            temp = temp%10;
            l1.val = temp;
            pre_1 = l1;
            pre_2 = l2;
            last = l1;
            l1 = l1.next;
            l2 = l2.next;
        }
        while(l1!=null){
            temp = l1.val+inc;
            inc = temp/10;
            temp = temp%10;
            l1.val = temp;
            last = l1;
            l1 = l1.next;
        }
        if(l2!=null){
            pre_2.next = null;
            pre_1.next = l2;
            while(l2!=null){
                temp = l2.val+inc;
                inc = temp/10;
                temp = temp%10;
                l2.val = temp;
                last = l2;
                l2 = l2.next;
            }
        }
        if(inc!=0){
            ListNode last_ = new ListNode(inc);
            last.next = last_;
        }
        return res;
    }
}