/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        ListNode head = new ListNode(-1);
        ListNode res = head;
        PriorityQueue<ListNode> minHeap = new PriorityQueue<ListNode>(new Comparator<ListNode>(){
            public int compare(ListNode l1,ListNode l2){
                return l1.val-l2.val;
            }
        });
        for(ListNode node:lists){
            if(node!=null) minHeap.offer(node);
        }
        while(!minHeap.isEmpty()){
            ListNode cur = minHeap.poll();
            ListNode temp = cur.next;
            cur.next = null;

            if(temp!=null) minHeap.offer(temp);
            head.next = cur;
            head = head.next;
        }
        return res.next;
    }
}