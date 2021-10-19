/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        int lengthA = 0;
        ListNode tA = headA;
        while(tA!=null){
            lengthA+=1;
            tA = tA.next;
        }
        int lengthB = 0;
        ListNode tB = headB;
        while(tB!=null){
            lengthB+=1;
            tB = tB.next;
        }

        if(lengthA>lengthB){
            int c = 0;
            while(c<lengthA-lengthB){
                headA = headA.next;
                c++;
            }
        }else{
            int c = 0;
            while(c<lengthB-lengthA){
                headB = headB.next;
                c++;
            }
        }

        while(headA!=null&&headB!=null){
            if(headA==headB) return headB;
            headA = headA.next;
            headB = headB.next;
        }
        return null;
    }
}