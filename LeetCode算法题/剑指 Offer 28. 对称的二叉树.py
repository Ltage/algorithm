# https://leetcode.cn/problems/dui-cheng-de-er-cha-shu-lcof/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 检查对应左右节点的相反子节点是否相同
class Solution:
    def check(self, a, b):
        if not a and not b:
            return True
        if not a or not b:
            return False
        if a.val == b.val:
            return self.check(a.left, b.right) and self.check(a.right, b.left)
        else:
            return False

    def isSymmetric(self, root: TreeNode) -> bool:
        return self.check(root, root)
