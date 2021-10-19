剑指offer55-1.二叉树的深度
----------
 - 题目
>输入一棵二叉树的根节点，求该树的深度。从根节点到叶节点依次经过的节点（含根、叶节点）形成树的一条路径，最长路径的长度为树的深度
>
 - 示例
 ----------
> input:
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
        def maxDepth(self, root: TreeNode) -> int:
            if root is None: return 0
            queue = [root]
            deep = 1
            last = root
            while queue:
                cur = queue[0]
                queue = queue[1:]
                if cur.left is not None:
                    queue.append(cur.left)
                if cur.right is not None:
                    queue.append(cur.right)
                if last==cur:
                    if queue:
                        last = queue[-1]
                        deep+=1
            return deep
  ----------
 - 解析
 > 求二叉树的深度用层序遍历;