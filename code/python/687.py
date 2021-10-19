# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        res = 0
        def dfs(node):
            nonlocal res
            if node is None:
                return 0
            length = 0
            # 取左边最长的
            leftL = dfs(node.left)
            # 取右边最长的
            rightL = dfs(node.right)
            # 以当前节点为根的最长
            if node.left is not None and node.right is not None and node.left.val==node.val and node.right.val==node.val:
                res = max(res,leftL+rightL+2)
            # 不以该节点为根，将左右两条链中长的拿去累加
            if node.left is not None and node.val==node.left.val:
                length = leftL+1
            if node.right is not None and node.val==node.right.val:
                length = max(length,rightL+1)
            res = max(res,length)
            return length
        dfs(root)
        if res==0:return 0
        return res