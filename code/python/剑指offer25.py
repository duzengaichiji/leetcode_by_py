# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = None
        last = None
        while l1 is not None and l2 is not None:
            if l1.val<=l2.val:
                node = ListNode(l1.val)
                l1 = l1.next
            else:
                node = ListNode(l2.val)
                l2 = l2.next
            if head is None:
                head = node
                last = node
            else:
                last.next = node
                last = node
            #print(head)
        if l1 is not None:
            if head is None:
                head = l1
            else:
                last.next = l1
        if l2 is not None:
            if head is None:
                head = l2
            else:
                last.next = l2
        return head