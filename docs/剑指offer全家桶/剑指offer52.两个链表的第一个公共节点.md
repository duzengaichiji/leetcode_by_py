剑指offer52.两个链表的第一个公共节点
----------
 - 题目
>输入两个链表，找出它们的第一个公共节点。
>
 - 示例
 ----------
> 
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
        def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
            lengthA = 0
            tA = headA
            while tA is not None:
                lengthA+=1
                tA = tA.next
            lengthB = 0
            tB = headB
            while tB is not None:
                lengthB+=1
                tB = tB.next
    
            if lengthA>lengthB:
                c = 0
                while c<lengthA-lengthB:
                    headA = headA.next
                    c+=1
            else:
                c = 0
                while c<lengthB-lengthA:
                    headB = headB.next
                    c+=1
            while headA is not None and headB is not None:
                if headA==headB:
                    return headA
                headA = headA.next
                headB = headB.next
            return None
  ----------
 - 解析
 > 
> 先计算两个链表的长度；
>
    lengthA = 0
    tA = headA
    while tA is not None:
        lengthA+=1
        tA = tA.next
    lengthB = 0
    tB = headB
    while tB is not None:
        lengthB+=1
        tB = tB.next
>
> 把长的那个向前移动一些，即将两个链表对齐，对齐之后寻找最前面那个相交节点即可；
>
>
    if lengthA>lengthB:
        c = 0
        while c<lengthA-lengthB:
            headA = headA.next
            c+=1
    else:
        c = 0
        while c<lengthB-lengthA:
            headB = headB.next
            c+=1