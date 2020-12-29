# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        que,curs = [],[]
        for index,node in enumerate(lists):
            if node is not None:
                heapq.heappush(que,(node.val,index))
            curs.append(node)

        head = ListNode(-1)
        current = head
        while que:
            num,index = heapq.heappop(que)
            current.next = curs[index]
            curs[index] = curs[index].next
            current = current.next
            if curs[index] is not None:
                heapq.heappush(que,(curs[index].val,index))
        return head.next