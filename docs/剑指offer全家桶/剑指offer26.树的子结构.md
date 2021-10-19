剑指offer26.二叉树的子结构
----------
 - 题目
>请输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)

B是A的子结构， 即 A中有出现和B相同的结构和节点值。

例如:
给定的树 A:

     3
    / \
   4   5
  / \
 1   2
给定的树 B：

   4 
  /
 1
返回 true，因为 B 与 A 的一个子树拥有相同的结构和节点值。

 - 示例
 ----------
> input: A = [1,2,3], B = [3,1]
> 
> output: false
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
        def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
            # B不能是空树
            if B is None:
                return False
            def isSub(a,b):
                # 排除各种两个节点不相同的情况
                if (a is None and b is not None) or (a is not None and b is None):
                    return False
                # 当前节点值都不相同，不用匹配剩下的部分
                if a.val!=b.val:
                    return False
                # 必须保证剩余的部分匹配成功
                left = True
                # b的子树不为空，则需要对比子树的结构
                if b.left is not None:
                    left = isSub(a.left,b.left)
                right =True
                if b.right is not None:
                    right = isSub(a.right,b.right)
                return left&right
            
            def fun(A,B):
                # 对每个节点进行子结构匹配
                if A is None:
                    return False
                if isSub(A,B)==True:
                    return True
                else:
                    return fun(A.left,B)|fun(A.right,B)
            return fun(A,B)
  ----------
 - 解析
 > 
> 显然，对A的每个节点对应的子树，都拿来和B匹配；
>
> 
>
    # A是空树则无需匹配
    if A is None:
        return False
    # 当前的A子树和B匹配成功
    if isSub(A,B)==True:
        return True
    # 否则分别匹配A的左子树以及右子树
    else:
        return fun(A.left,B)|fun(A.right,B)