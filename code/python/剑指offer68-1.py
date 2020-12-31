# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        res = None
        def dfs(node):
            nonlocal res
            if node is None:
                return None
            if node==p:
                if dfs(node.left) is not None or dfs(node.right) is not None:
                    res = node if res is None else res
                return node
            if node==q:
                if dfs(node.left) is not None or dfs(node.right) is not None:
                    res = node if res is None else res
                return node
            getp = dfs(node.left)
            getq = dfs(node.right)
            if getp is not None and getq is not None:
                res = node if res is None else res
                return node
            elif getp is not None or getq is not None:
                return node
            else:
                return None

        dfs(root)
        return res