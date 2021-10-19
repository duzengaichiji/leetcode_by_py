剑指offer68-1.二叉树的最近公共祖先
----------
 - 题目
>给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。

>百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。
 - 示例
 ----------
>input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8

> output: 6 
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
        def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
            res = None
            def dfs(node):
                nonlocal res
                if node is None:
                    return None
                # 如果当前节点是p，检查它的子孙中是否存在q；
                # 如果存在则p节点就是最近公共祖先，如果不存在，则返回本节点以表示在该子树中找到了p
                if node==p:
                    if dfs(node.left) is not None or dfs(node.right) is not None:
                        res = node if res is None else res
                    return node
                # 如果当前节点是q，检查它的子孙中是否存在q；
                # 和上面一样
                if node==q:
                    if dfs(node.left) is not None or dfs(node.right) is not None:
                        res = node if res is None else res
                    return node
                # 如果当前节点既不是p，也不是q，则检查它的左，右子孙；
                # 如果恰好一边有p，一边有q，则该节点就是最近公共祖先；
                # 如果只有一个，返回当前节点表示在该节点的子树下找到了p或者q
                # 如果没有，则返回None表示当前子树下什么都没有
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
 ----------
 - 解析
 >
> 基本框架是后续遍历，先检查左，右子树中是否存在p以及q，就可以得到当前节点是否是塔门的最近公共祖先；
>
> 其他细节看注释；