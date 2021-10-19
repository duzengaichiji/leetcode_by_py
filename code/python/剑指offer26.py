# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if B is None:
            return False

        def isSub(a, b):
            if (a is None and b is not None) or (a is not None and b is None):
                return False
            if a.val != b.val:
                return False
            left = True
            if b.left is not None:
                left = isSub(a.left, b.left)
            right = True
            if b.right is not None:
                right = isSub(a.right, b.right)
            return left & right

        def fun(A, B):
            if A is None:
                return False
            if isSub(A, B) == True:
                return True
            else:
                return fun(A.left, B) | fun(A.right, B)

        return fun(A, B)