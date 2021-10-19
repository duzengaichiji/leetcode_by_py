剑指offer28.对称的二叉树
----------
 - 题目
>
>请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的。
>
>例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
>
>    1
>   / \
>  2   2
> / \ / \
>3  4 4  3
>
>但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
>
>    1
>   / \
>  2   2
>   \   \
>   3    3
>
>
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
            def symTree(left,right):
                if left is None and right is None:
                    return True
                if (left is not None and right is None) or \
                    (left is None and right is not None):
                    return False
                if left.val!=right.val:
                    return False
                return symTree(left.left,right.right) and symTree(left.right,right.left)
            return root is None or symTree(root.left,root.right)
  ----------
 - 解析
 > 
> 构造原树的镜像，对比二者是否完全相同即可;