# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None: return 0
        queue = [root]
        deep = 1
        last = root
        while queue:
            cur = queue[0]
            queue = queue[1:]
            if cur.left is not None:
                queue.append(cur.left)
            if cur.right is not None:
                queue.append(cur.right)
            if last==cur:
                if queue:
                    last = queue[-1]
                    deep+=1
        return deep