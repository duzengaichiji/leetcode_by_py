"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None: return None
        originToCopy = {}
        temp = head
        last = None
        while temp is not None:
            node = Node(temp.val)
            if last is None:
                last = node
            else:
                last.next = node
                last = node
            originToCopy[temp] = node
            temp = temp.next

        temp = head
        while temp is not None:
            #print(temp.val,temp.random)
            if temp.random is None:
                originToCopy[temp].random = None
            else:
                originToCopy[temp].random = originToCopy[temp.random]
            temp = temp.next
        return originToCopy[head]

