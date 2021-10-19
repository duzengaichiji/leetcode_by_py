剑指offer07.重建二叉树
----------
 - 题目
>输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
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
 ----------
 - 解析
 >
> 我们知道，由二叉树的 （前序+中序），（中序+后续）可以重建二叉树，因为它们可以唯一地确定一棵二叉树；
>
> 这类重建，统一用递归；
>
> 其核心思想是，**确定左右子树在遍历数组中的范围**；
>
 ----------
> 首先，前序遍历中，**根节点总是出现在子节点之前**，而中序遍历中，**根节点总是出现在左，右子树之间**；
>
> 有了这个条件，很容易得到左右子树在前序数组和中序数组中对应的范围；
>
> 传入的数组范围中，前序遍历的第一个，就是当前要重建的子树的根节点，因此当前要拿这个值建立一个节点；
>
    node = TreeNode(preOrder[0])
>
> 然后，去中序中找出这个节点，就能确定该子树的左子树范围和右子树范围；
>
> 
    while inOrder[i]!=preOrder[0]:
        i+=1
> 由这个i可以确定左，右子树的范围，对左，右子树递归的进行该过程，建立左，右子树，并将它们挂到当前节点下面；
>
    node.left = buildtree(preOrder[1:i+1],inOrder[:i],node)
    node.right = buildtree(preOrder[i+1:],inOrder[i+1:],node)