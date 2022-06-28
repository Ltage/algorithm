# https://leetcode.cn/problems/find-largest-value-in-each-tree-row/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# BFS
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if not root:
            return ans
        q = [root]
        while q:
            max_val = -inf
            next_q = []
            while len(q) > 0:
                cur_node = q.pop(0)
                max_val = max(max_val, cur_node.val)
                if cur_node.left:
                    next_q.append(cur_node.left)
                if cur_node.right:
                    next_q.append(cur_node.right)
            ans.append(max_val)
            q = next_q
        return ans