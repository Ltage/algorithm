# https://leetcode.cn/problems/find-bottom-left-tree-value/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        # įŽåéå
        q = [root]
        while q:
            ans = q.pop(0)
            if ans.right:
                q.append(ans.right)
            if ans.left:
                q.append(ans.left)

        return ans.val
