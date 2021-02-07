"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if root is None: return None
        stack = []
        res = []
        cur = root
        while True:
            while cur is not None:
                stack.append(cur)
                cur = cur.left
            if stack:
                cur = stack.pop()
            else:
                break
            res.append(cur)
            if cur.right is not None:
                cur = cur.right
            else:
                cur = None
        head = res[0]
        head.left = res[-1]
        pre = head
        for i in range(1,len(res)):
            res[i].left = pre
            pre.right = res[i]
            pre = res[i]
        res[-1].right = head
        return head
