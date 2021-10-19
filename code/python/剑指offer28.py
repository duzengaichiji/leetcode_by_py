# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def symTree(root):
            if root is not None:
                new_root = TreeNode(root.val)
                if root.left is not None:
                    new_root.right = symTree(root.left)
                if root.right is not None:
                    new_root.left = symTree(root.right)
                return new_root
            return None
        def judge(root1,root2):
            if root1 is None and root2 is None:
                return True
            if root1 is None and root2 is not None:
                return False
            if root2 is None and root1 is not None:
                return False
            if root1.val!=root2.val:
                return False
            left = True
            if root1.left is not None:
                left = judge(root1.left,root2.left)
            right = True