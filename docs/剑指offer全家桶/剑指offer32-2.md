剑指offer32-2.从上到下打印二叉树Ⅱ
----------
 - 题目
>从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。
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
        def levelOrder(self, root: TreeNode) -> List[List[int]]:
            if root is None:
                return []
            result = [[]]
            queue = []
            queue.append(root)
            last = root
            while queue:
                cur = queue[0]
                queue = queue[1:]
                result[-1].append(cur.val)
                if cur.left is not None:
                    queue.append(cur.left)
                if cur.right is not None:
                    queue.append(cur.right)
                if cur==last:
                    if queue:
                        result.append([])
                        last = queue[-1]
            return result

    
  ----------
 - 解析
 >