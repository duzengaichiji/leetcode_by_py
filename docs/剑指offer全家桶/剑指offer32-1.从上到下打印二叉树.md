剑指offer32-1.从上到下打印二叉树
----------
 - 题目
>从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。
 - 示例
 ----------
> input: 
> 
> output: 就是层序遍历
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
        def levelOrder(self, root: TreeNode) -> List[int]:
            if root is None: return []
    
            res = []
            queue = [root]
            while queue:
                cur = queue[0]
                res.append(cur.val)
                queue = queue[1:]
                if cur.left is not None:
                    queue.append(cur.left)
                if cur.right is not None:
                    queue.append(cur.right)
            return res

    
  ----------
 - 解析
 >