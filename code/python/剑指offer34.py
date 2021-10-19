# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res = []
        def dfs(node,path,value):
            path.append(node.val)
            value+=node.val
            if value==sum:
                if node.left is None and node.right is None:
                    res.append(path.copy())
            if node.left is not None:
                dfs(node.left,path,value)
            if node.right is not None:
                dfs(node.right,path,value)
            path.pop()
            value-=node.val
        if root is None:
            return []
        dfs(root,[],0)
        return res