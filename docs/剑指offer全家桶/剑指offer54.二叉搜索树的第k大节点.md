剑指offer54.二叉搜索树的第k大节点
----------
 - 题目
>给定一棵二叉搜索树，请找出其中第k大的节点。
>
 - 示例
 ----------
> 
 ----------
 - 代码
 >
>
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
  ----------
 - 解析
 > 
> 二叉搜索树按照中序遍历就是递增的，因此，直接采用非递归形式的中序遍历即可；
>
> 当然，也可以采取反序的中序遍历，这样到第k个就是答案了；