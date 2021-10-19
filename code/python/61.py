# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is None or head.next is None: return head

        length = 0
        p = head
        while p is not None:
            length += 1
            p = p.next

        k = k % length
        if k == 0: return head

        left = length - k
        pre = head
        cur = head
        c = 0
        while c < left:
            pre = cur
            cur = cur.next
            c += 1
        pre.next = None
        res = cur
        while cur.next is not None:
            cur = cur.next
        cur.next = head
        return res

