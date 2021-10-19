剑指offer36.二叉树与双向链表
----------
 - 题目
>输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回 true，否则返回 false。假设输入的数组的任意两个数字都互不相同。
 - 示例
 ----------
> input: [1,6,3,2,5]
> 
> output: false
 ----------
 - 代码
 >
>
    """
    # Definition for a Node.
    class Node:
        def __init__(self, val, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
    """
    class Solution:
        def treeToDoublyList(self, root: 'Node') -> 'Node':
            if root is None: return None
            stack = []
            res = []
            cur = root
            while True:
                while cur is not None:
                    stack.append(cur)
                    cur = cur.left
                if stack:
                    cur = stack.pop()
                else:
                    break
                res.append(cur)
                if cur.right is not None:
                    cur = cur.right
                else:
                    cur = None
            head = res[0]
            head.left = res[-1]
            pre = head
            for i in range(1,len(res)):
                res[i].left = pre
                pre.right = res[i]
                pre = res[i]
            res[-1].right = head
            return head
    
  ----------
 - 解析
 > 二叉搜索树按照中序遍历拆下来，然后按顺序拼接成为双向链表即可；
> 
> 