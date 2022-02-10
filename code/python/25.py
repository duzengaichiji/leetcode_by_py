# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(root, k):
            cur = root
            idx = 1
            while cur and idx < k:
                cur = cur.next
                idx += 1
            # 长度不够，直接返回
            if idx < k or cur is None:
                return root,root, None
            # 截断最后一个node与后面节点的连接
            post = cur.next
            cur.next = None
            # 头插法逆转当前截断的链表
            vituralNode = ListNode(-1)
            cur = root
            while cur:
                temp = cur.next
                cur.next = None
                cur.next = vituralNode.next
                vituralNode.next = cur
                cur = temp
            head = vituralNode.next
            vituralNode.next = None
            return head,root, post
        if not head or k == 0: return head
        res = []
        # 分段反转链表，长度不够就表示到头了
        while True:
            headN,endN,postN = reverse(head, k)
            res.append((headN,endN))
            if postN is None: break
            head = postN
        # 分段的链表头尾相连
        lastEnd = None
        for headN,endN in res:
            if lastEnd:
                lastEnd.next = headN
            lastEnd = endN
        return res[0][0]

