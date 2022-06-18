# https://leetcode.cn/problems/most-frequent-subtree-sum/
# DFS + HASH
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        res = defaultdict(int)

        def dfs(node):
            if not node:
                return 0
            node.val += dfs(node.left) + dfs(node.right)
            res[node.val] += 1
            return node.val

        dfs(root)
        max_cnt = max(res.values())
        return [ans for ans, cnt in res.items() if cnt == max_cnt]


