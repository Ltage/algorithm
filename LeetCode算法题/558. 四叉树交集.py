# https://leetcode.cn/problems/logical-or-of-two-binary-grids-represented-as-quad-trees/
# 递归
# 逻辑或：a | b
# ①如果a=b=1返回a或b均可，②如果其中一个为0，返回另一个的值
"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def intersect(self, t1: 'Node', t2: 'Node') -> 'Node':
        if t1.isLeaf:
            return t1 if t1.val else t2
        if t2.isLeaf:
            return t2 if t2.val else t1
        n1 = self.intersect(t1.topLeft, t2.topLeft)
        n2 = self.intersect(t1.topRight, t2.topRight)
        n3 = self.intersect(t1.bottomLeft, t2.bottomLeft)
        n4 = self.intersect(t1.bottomRight, t2.bottomRight)
        if n1.val == n2.val == n3.val == n4.val and n1.isLeaf and n2.isLeaf and n3.isLeaf and n4.isLeaf:
            return Node(n1.val, 1, None, None, None, None)
        return Node(0, 0, n1, n2, n3, n4)