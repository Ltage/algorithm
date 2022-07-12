# https://leetcode.cn/problems/fu-za-lian-biao-de-fu-zhi-lcof/
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
        # 空节点直接返回
        if not head:
            return None

        # 初始化根节点
        root = Node(head.val)

        # 为原链表的每个结点计算从头结点到其random结点的距离
        h = head
        dis = []
        while h:
            temp = 0
            cur = head
            if h.random == None:
                dis.append(-1)
            else:
                while h.random != cur:
                    temp += 1
                    cur = cur.next
                dis.append(temp)
            h = h.next

        # 不考虑random，先将链表组建起来
        r = root
        h = head
        while h.next:
            r.val = h.val
            r.next = Node(h.next.val)
            r = r.next
            h = h.next
        r.next = None

        # 将结点映射到数组里
        r = root
        node = []
        while r:
            node.append(r)
            r = r.next

        # 根据dis与node确定random应指向的节点
        r = root
        i = 0
        while r:
            if dis[i] == -1:
                r.random = None
            else:
                r.random = node[dis[i]]
            r = r.next
            i += 1

        return root


