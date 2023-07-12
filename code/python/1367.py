class Solution:
    def dfs(self, head: ListNode, rt: TreeNode) -> bool:
        if not head:
            return True
        if not rt:
            return False
        if rt.val != head.val:
            return False
        return self.dfs(head.next, rt.left) or self.dfs(head.next, rt.right)

    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        if not root:
            return False
        return self.dfs(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)