# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        def reverse(node):
            if node is None:
                return node
            if node.left is not None:
                node.left = reverse(node.left)
            if node.right is not None:
                node.right = reverse(node.right)
            if node.left is not None or node.right is not None:
                temp = node.left
                node.left = node.right
                node.right = temp
            return node
        return reverse(root)