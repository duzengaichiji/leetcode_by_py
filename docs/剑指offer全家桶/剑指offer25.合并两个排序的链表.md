剑指offer25.合并两个排序的链表
----------
 - 题目
>输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。
 - 示例
 ----------
>input: 1->2->4, 1->3->4

> output: 1->1->2->3->4->4
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
        def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
            head = None
            last = None
            while l1 is not None and l2 is not None:
                if l1.val<=l2.val:
                    node = ListNode(l1.val)
                    l1 = l1.next
                else:
                    node = ListNode(l2.val)
                    l2 = l2.next
                if head is None:
                    head = node
                    last = node
                else:
                    last.next = node
                    last = node
                #print(head)
            if l1 is not None:
                if head is None:
                    head = l1
                else:
                    last.next = l1
            if l2 is not None:
                if head is None:
                    head = l2
                else:
                    last.next = l2
            return head
  ----------
 - 解析
 > 
> 