剑指offer32-2.从上到下打印二叉树Ⅲ
----------
 - 题目
>请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。
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
            for i in range(len(result)):
                if i%2==1:
                    result[i] = result[i][::-1]
            return result

    
  ----------
 - 解析
 >