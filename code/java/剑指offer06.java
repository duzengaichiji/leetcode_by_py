/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public int[] reversePrint(ListNode head) {
        List<Integer> res = new ArrayList<>();
        while(head!=null){
            res.add(head.val);
            head =head.next;
        }
        int[] result = new int[res.size()];
        for(int i=0;i<res.size();i++){
            result[res.size()-i-1] = res.get(i);
        }
        return result;
    }
}