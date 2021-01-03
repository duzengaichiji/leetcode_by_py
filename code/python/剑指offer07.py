# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def buildtree(preOrder,inOrder,root):
            if len(preOrder)==0:
                return None
            node = TreeNode(preOrder[0])
            i = 0
            while inOrder[i]!=preOrder[0]:
                i+=1
            node.left = buildtree(preOrder[1:i+1],inOrder[:i],node)
            node.right = buildtree(preOrder[i+1:],inOrder[i+1:],node)
            return node
        root = buildtree(preorder,inorder,None)
        return root