# https://leetcode.cn/problems/cong-shang-dao-xia-da-yin-er-cha-shu-iii-lcof/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        ans = []
        s = [root]
        next_s = []
        flag = True
        while s:
            ans.append([])
            for _ in range(len(s)):
                node = s.pop()
                ans[-1].append(node.val)
                if flag:
                    if node.left:
                        next_s.append(node.left)
                    if node.right:
                        next_s.append(node.right)
                else:
                    if node.right:
                        next_s.append(node.right)
                    if node.left:
                        next_s.append(node.left)
            s, next_s = next_s, s
            flag = not flag
        return ans