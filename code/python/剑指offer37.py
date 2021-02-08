# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return []
        res = []
        queue = [root]
        while queue:
            cur = queue[0]
            queue = queue[1:]
            if cur is not None:
                res.append(cur.val)
                queue.append(cur.left)
                queue.append(cur.right)
            else:
                # 不添加空节点的左右节点
                res.append(None)
        for i in range(len(res) - 1, -1, -1):
            if res[i] is not None:
                break
        res = res[:i + 1]
        return res

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        # print(data)
        root = TreeNode(data[0])
        queue = [root]
        index = 0
        # 按照层序遍历构建二叉树
        while index < len(data):
            cur = queue[0]
            queue = queue[1:]
            index += 1
            if index < len(data):
                if data[index] is not None:
                    cur.left = TreeNode(data[index])
                    queue.append(cur.left)
                else:
                    cur.left = None
            index += 1
            if index < len(data):
                if data[index] is not None:
                    cur.right = TreeNode(data[index])
                    queue.append(cur.right)
                else:
                    cur.right = None
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))