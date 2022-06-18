# https://leetcode.cn/problems/4ueAj6/
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: "Node", insertVal: int) -> 'Node':
        node = Node(insertVal)
        ans = head

        # 节点为空（case 1）
        if head is None:
            node.next = node
            return node

        # 所有节点val值相等（case 2）
        while head.val == head.next.val:
            head = head.next
            if ans == head:
                node.next = head.next
                head.next = node
                return ans

        # 找出最大节点
        while head.val <= head.next.val:
            head = head.next
        if (head.val >= node.val and node.val <= head.next.val) or node.val >= head.val:  # 插入值为最小或最大（case 3）
            node.next = head.next
            head.next = node
            return ans

        # 插入值处于不大不小的位置，放入中间（case 4）
        while not (head.val <= node.val <= head.next.val):
            head = head.next
        node.next = head.next
        head.next = node
        return ans