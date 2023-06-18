

"""
前序遍历
"""

# 递归版
def preorderTraversal(self, root: TreeNode) -> List[int]:
    res = []

    def preordertraversal(node):
        if not node:
            return
        res.append(node.val)
        preordertraversal(node.left)
        preordertraversal(node.right)

    preordertraversal(root)
    return res

# 非递归版
def preorderTraversal(self, root: TreeNode) -> List[int]:
    if root is None:
        return []
    stack = [root]
    res = []
    while stack:
        cur = stack.pop()
        while cur is not None:
            res.append(cur.val)
            if cur.right is not None:
                stack.append(cur.right)
            cur = cur.left
    return res

"""
中序遍历
"""

# 递归版
def inorderTraversal(self, root: TreeNode) -> List[int]:
    res = []

    def inordertraversal(node):
        if node is None:
            return
        inordertraversal(node.left)
        res.append(node.val)
        inordertraversal(node.right)

    inordertraversal(root)
    return res

# 非递归版
def inorderTraversal(self, root: TreeNode) -> List[int]:
    if root is None:
        return []
    result = []
    stack = []
    while len(stack) > 0 or root is not None:
        while root is not None:
            stack.append(root)
            root = root.left
        root = stack[-1]
        result.append(root.val)
        stack = stack[:-1]
        root = root.right
    return result

"""
后序遍历
"""

# 递归版
def postorderTraversal(self, root: TreeNode) -> List[int]:
    res = []

    def postordertraversal(node):
        if node is None:
            return
        postordertraversal(node.left)
        postordertraversal(node.right)
        res.append(node.val)

    postordertraversal(root)
    return res

# 非递归版
def postorderTraversal(self, root: TreeNode) -> List[int]:
    if root is None:
        return []
    stack = []
    res = []
    # 给每个节点赋予一个标记，标记它的右子树是否被遍历过；
    stack.append((root, True))
    cur = root.left
    while stack:
        while cur is not None:
            stack.append((cur, True))
            cur = cur.left
        cur, rightOrNot = stack.pop()
        if rightOrNot == True:
            if cur.right is not None:
                stack.append((cur, False))
                cur = cur.right
                continue
            else:
                res.append(cur.val)
                cur = None
        else:
            res.append(cur.val)
            cur = None

    return res