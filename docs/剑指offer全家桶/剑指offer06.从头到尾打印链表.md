剑指offer06.从头到尾打印链表
----------
 - 题目
>输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。
 - 示例
 ----------
>input: head = [1,3,2]

> output: [2,3,1]
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
        def reversePrint(self, head: ListNode) -> List[int]:
            stack = []
            while head!=None:
                stack.append(head.val)
                head = head.next
            return stack[::-1]
 ----------
 - 解析
 > 也可以用stack，逆序输出；