剑指offer28.对称的二叉树
----------
 - 题目
>
难度
简单

121





请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3

 - 示例
 ----------
> input: root = [1,2,2,3,4,4,3]
> 
> output: true
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
        def isSymmetric(self, root: TreeNode) -> bool:
            def symTree(root):
                if root is not None:
                    new_root = TreeNode(root.val)
                    if root.left is not None:
                        new_root.right = symTree(root.left)
                    if root.right is not None:
                        new_root.left = symTree(root.right)
                    return new_root
                return None
            def judge(root1,root2):
                if root1 is None and root2 is None:
                    return True
                if root1 is None and root2 is not None:
                    return False
                if root2 is None and root1 is not None:
                    return False
                if root1.val!=root2.val:
                    return False
                left = True
                if root1.left is not None:
                    left = judge(root1.left,root2.left)
                right = True
            new_tree = symTree(root)
            return judge(root,new_tree)
  ----------
 - 解析
 > 
> 构造原树的镜像，对比二者是否完全相同即可;