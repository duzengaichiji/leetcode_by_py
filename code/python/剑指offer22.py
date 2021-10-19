# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        if head is None:
            return None
        length = 0
        result = None
        temp = head
        while head is not None:
            length+=1
            if length>=k:
                if result is None:
                    result = temp
                else:
                    result = result.next
            #print(length,result)
            head = head.next
        return result