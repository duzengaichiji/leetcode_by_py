剑指offer27.二叉树的镜像
----------
 - 题目
>请完成一个函数，输入一个二叉树，该函数输出它的镜像。

例如输入：

     4
   /   \
  2     7
 / \   / \
1   3 6   9
镜像输出：

     4
   /   \
  7     2
 / \   / \
9   6 3   1

 - 示例
 ----------
> input: root = [4,2,7,1,3,6,9]
> 
> output: [4,7,2,9,6,3,1]
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
        def mirrorTree(self, root: TreeNode) -> TreeNode:
            def reverse(node):
                if node is None:
                    return node
                if node.left is not None:
                    node.left = reverse(node.left)
                if node.right is not None:
                    node.right = reverse(node.right)
                # 交换左右子树
                if node.left is not None or node.right is not None:
                    temp = node.left
                    node.left = node.right
                    node.right = temp
                return node
            return reverse(root)
  ----------
 - 解析
 > 
> 采用后序遍历，自下而上的不停交换左右子树；