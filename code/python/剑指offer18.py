# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if head.next is None:
            return None
        if head.val==val:
            return head.next
        last = head
        cur = head.next
        while cur.val!=val:
            last = cur
            cur = cur.next
        last.next = cur.next
        return head