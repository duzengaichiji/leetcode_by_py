# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def balance(root):
            if root is None: return 0,True
            if root.left is not None:
                left,l = balance(root.left)
            else:
                left,l = 0,True
            if root.right is not None:
                right,r = balance(root.right)
            else:
                right,r = 0,True
            return max(left,right)+1,l and r and abs(left-right)<=1
        return balance(root)[1]
