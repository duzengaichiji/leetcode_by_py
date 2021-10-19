剑指offer34.二叉树中和为某一值的路径
----------
 - 题目
>输入一棵二叉树和一个整数，打印出二叉树中节点值的和为输入整数的所有路径。从树的根节点开始往下一直到叶节点所经过的节点形成一条路径。
 - 示例
 ----------
> input: 一棵树和sum=?;
> 
> output: 值为sum的所有路径
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
        def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
            res = []
            def dfs(node,path,value):
                """
                    path:记录已经访问过的节点
                    value:暂存当前的路径和
                """
                path.append(node.val)
                value+=node.val
                if value==sum:
                    # 当前路径和为目标值，记录路径列表
                    if node.left is None and node.right is None:
                        res.append(path.copy())
                # 尝试所有路径
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
    

    
  ----------
 - 解析
 > 典型dfs应用；
> 
> 