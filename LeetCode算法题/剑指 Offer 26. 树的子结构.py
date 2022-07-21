# https://leetcode.cn/problems/shu-de-zi-jie-gou-lcof/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 先找到相同值的点，再对两个点进行check
class Solution:
    def check(self, a, b):
        if not b:
            return True
        if not a:
            return False
        if a.val == b.val:
            return self.check(a.left, b.left) and self.check(a.right, b.right)
        else:
            return False

    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if not A:
            return False
        if not B:
            return False
        if A.val == B.val:
            return self.check(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)
        else:
            return self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)