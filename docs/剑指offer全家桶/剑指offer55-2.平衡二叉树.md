剑指offer55-2.平衡二叉树
----------
 - 题目
>输入一棵二叉树的根节点，判断该树是不是平衡二叉树。如果某二叉树中任意节点的左右子树的深度相差不超过1，那么它就是一棵平衡二叉树。
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
        def isBalanced(self, root: TreeNode) -> bool:
            def balance(root):
                if root is None: return 0,True
                if root.left is not None:
                    left,l = balance(root.left)
                else:
                    left,l = 0,True
                if root.right is not None:
                    right,r = balance(root.right)
                else:
                    right,r = 0,True
                # 返回当前节点地判定结果以及当前节点地最大高度
                return max(left,right)+1,l and r and abs(left-right)<=1
            return balance(root)[1]

  ----------
 - 解析
 > 要判断一棵树是否为平衡二叉树，就要判断所有分支节点的左右子树高度差是否<=1；
>
> 这种情况下，显然需要递归地从下而上进行判断；
>
> 因为高度是自下而上不断累加地；
>
> 当有一个分支节点不是平衡节点时，会返回False；
>
> 则该节点上面的所有节点的判定结果均为false;