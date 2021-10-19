剑指offer37.序列化二叉树
----------
 - 题目
>请实现两个函数，分别用来序列化和反序列化二叉树
 - 示例
 ----------
> input: 
> 
> output: 
 ----------
 - 代码
 >
>
> 
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
            # 基本结构是层序遍历
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
                    # 如果该节点为空，添加一个空 作为标记
                    res.append(None)
            for i in range(len(res)-1,-1,-1):
                if res[i] is not None:
                    break
            res = res[:i+1]
            return res
            
    
        def deserialize(self, data):
            """Decodes your encoded data to tree.
            
            :type data: str
            :rtype: TreeNode
            """
            if not data:
                return None
            # 层序遍历的首位是根节点
            root = TreeNode(data[0])
            queue = [root]
            index = 0
            # 一层一层构建二叉树
            while index<len(data):
                cur = queue[0]
                queue = queue[1:]
                # 此时index会指向cur的左儿子位置
                index+=1
                if index<len(data):
                    if data[index] is not None:
                        cur.left = TreeNode(data[index])
                        queue.append(cur.left)
                    else:
                        cur.left = None
                index+=1
                if index<len(data):
                    if data[index] is not None:
                        cur.right = TreeNode(data[index])
                        queue.append(cur.right)
                    else:
                        cur.right = None
            return root
            
    
    # Your Codec object will be instantiated and called as such:
    # codec = Codec()
    # codec.deserialize(codec.serialize(root))
  ----------
 - 解析
 > 
> 按照题目的要求，其实序列化的时候不是按照完全二叉树去存储；
> 
> 只要满足反序列化之后能变得回来就行；