剑指offer18.删除链表的节点
----------
 - 题目
>给定单向链表的头指针和一个要删除的节点的值，定义一个函数删除该节点。

>返回删除后的链表的头节点。

>注意：此题对比原题有改动
 - 示例
 ----------
>input: head = [4,5,1,9], val = 5

> output: [4,1,9]
 ----------
 - 代码
 >
>
    # Definition for singly-linked list.
    # class ListNode:
    #     def __init__(self, x):
    #         self.val = x
    #         self.next = None
    class Solution:
        def deleteNode(self, head: ListNode, val: int) -> ListNode:
            if head.next is None:
                return None
            if head.val==val:
                return head.next
            last = head
            cur = head.next
            while cur.val!=val:
                last = cur
                cur = cur.next
            last.next = cur.next
            return head
  ----------
 - 解析
 > 