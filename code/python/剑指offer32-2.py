# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        result = [[]]
        queue = []
        queue.append(root)
        last = root
        while queue:
            cur = queue[0]
            queue = queue[1:]
            result[-1].append(cur.val)
            if cur.left is not None:
                queue.append(cur.left)
            if cur.right is not None:
                queue.append(cur.right)
            if cur==last:
                if queue:
                    result.append([])
                    last = queue[-1]
        return result