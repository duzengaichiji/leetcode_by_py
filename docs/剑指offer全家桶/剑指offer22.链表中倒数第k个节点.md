剑指offer22.链表中倒数第k个节点
----------
 - 题目
>输入一个链表，输出该链表中倒数第k个节点。为了符合大多数人的习惯，本题从1开始计数，即链表的尾节点是倒数第1个节点。例如，一个链表有6个节点，从头节点开始，它们的值依次是1、2、3、4、5、6。这个链表的倒数第3个节点是值为4的节点。
 - 示例
 ----------
>input: 给定一个链表: 1->2->3->4->5, 和 k = 2.

> output: 返回链表 4->5
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
        def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
            if head is None:
                return None
            length = 0
            result = None
            temp = head
            while head is not None:
                length+=1
                if length>=k:
                    if result is None:
                        result = temp
                    else:
                        result = result.next
                #print(length,result)
                head = head.next
            return result
  ----------
 - 解析
 > 
> 利用双指针；
>
> 当第一个指针走到第k个节点的时候，将第二个指针指向头节点；
> 
>  两个一起移动，直至远的那个节点到尾部，则另一个节点指向倒数第k个节点；