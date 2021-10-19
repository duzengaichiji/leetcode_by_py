剑指offer35.复杂链表的复制
----------
 - 题目
>请实现 copyRandomList 函数，复制一个复杂链表。在复杂链表中，每个节点除了有一个 next 指针指向下一个节点，还有一个 random 指针指向链表中的任意节点或者 null。
 - 示例
 ----------
> input: 
> 
> output: 
 ----------
 - 代码
 >
>
    """
    # Definition for a Node.
    class Node:
        def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
            self.val = int(x)
            self.next = next
            self.random = random
    """
    class Solution:
        def copyRandomList(self, head: 'Node') -> 'Node':
            if head is None: return None
            originToCopy = {}
            temp = head
            last = None
            # 复制原始链表，记录 原始/复制 的对应关系
            while temp is not None:
                node = Node(temp.val)
                if last is None:
                    last = node
                else:
                    last.next = node
                    last = node
                originToCopy[temp] = node
                temp = temp.next
            # 复制random指针的关系
            temp = head
            while temp is not None:
                #print(temp.val,temp.random)
                if temp.random is None:
                    originToCopy[temp].random = None
                else:
                    originToCopy[temp].random = originToCopy[temp.random]
                temp = temp.next
            return originToCopy[head]

    
  ----------
 - 解析
 > 
> 最简单且容易想到的办法，就是逐个遍历，并且建立新的节点；
> 
> 之后再将复制链表的random指针指向正确的位置；
> 
> 这期间，需要用哈希表记录每个节点对应的复制节点，就可以轻易的将random指向正确位置；
> 
> 
----------
> 
    """
    # Definition for a Node.
    class Node:
        def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
            self.val = int(x)
            self.next = next
            self.random = random
    """
    class Solution:
        def copyRandomList(self, head: 'Node') -> 'Node':
            if head is None: return None
            temp = head
            # 在原始链表中插入复制节点
            while temp is not None:
                post = temp.next
                node = Node(temp.val)
                temp.next = node
                node.next = post
                temp = post
            # 赋予random连接
            temp = head
            while temp is not None:
                copy = temp.next
                if temp.random is not None:
                    copy.random = temp.random.next
                else:
                    copy.random = None
                temp = temp.next.next
            # 拆分链表
            cur = res = head.next
            pre = head
            while cur.next:
                pre.next = pre.next.next
                cur.next = cur.next.next
                pre = pre.next
                cur = cur.next
            pre.next = None # 单独处理原链表尾节点
            return res      # 返回新链表头节点
>
> 
> 更好的解法是不需要利用哈希表的；
> 
> 将整个过程分为三步；
> 
> 1.创建原链表的复制链表，将它们挂在原节点后面，即；
> 
> node1->copy_node1->node2->copy_node2.....；
> 
> 这样，每个节点的复制节点都可以通过 node.next直接找到；
> 
> 2.遍历原节点，并将它们的random赋予给对应的复制节点；
> 
> 3.拆分两个链表；