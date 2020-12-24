# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        result = 0
        def solve(node):
            nonlocal result
            if node is None:
                return 2
            left = solve(node.left)
            right = solve(node.right)
            if left==2 and right==2:
                return 0
            if left==0 or right==0:
                result+=1
                return 1
            if left==1 or right==1:
                return 2
            return
        if solve(root)==0:
            result+=1
        return result