剑指offer24.反转链表
----------
 - 题目
>定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。
 - 示例
 ----------
>input: 1->2->3->4->5->NULL

> output: 5->4->3->2->1->NULL
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
        def reverseList(self, head: ListNode) -> ListNode:
            if head is None: return head
            pre = head
            head = head.next
            pre.next = None
    
            while head is not None:
                temp = head.next
                head.next = pre
                pre = head
                head = temp
            return pre
  ----------
 - 解析
 > 
> 