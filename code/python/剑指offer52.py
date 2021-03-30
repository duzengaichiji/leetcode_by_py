# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        lengthA = 0
        tA = headA
        while tA is not None:
            lengthA+=1
            tA = tA.next
        lengthB = 0
        tB = headB
        while tB is not None:
            lengthB+=1
            tB = tB.next

        if lengthA>lengthB:
            c = 0
            while c<lengthA-lengthB:
                headA = headA.next
                c+=1
        else:
            c = 0
            while c<lengthB-lengthA:
                headB = headB.next
                c+=1
        while headA is not None and headB is not None:
            if headA==headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None