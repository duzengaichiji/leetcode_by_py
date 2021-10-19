# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        c = 0
        stack = []
        res = []
        while True:
            while root is not None:
                stack.append(root)
                root = root.left
            if not stack:
                break
            root = stack.pop()
            res.append(root.val)
            if root.right is not None:
                root = root.right
            else:
                root = None
        return res[-k]