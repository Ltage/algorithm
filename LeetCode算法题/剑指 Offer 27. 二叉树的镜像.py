# https://leetcode.cn/problems/er-cha-shu-de-jing-xiang-lcof/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 递归，左右互换
class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if root:
            root.left, root.right = root.right, root.left
            self.mirrorTree(root.left)
            self.mirrorTree(root.right)
        return root