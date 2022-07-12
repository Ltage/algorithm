# https://leetcode.cn/problems/minimum-cost-to-move-chips-to-the-same-position/
# 他太简单了
class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        a = 0
        b = 0
        for i in position:
            if i & 1:
                a += 1
            else:
                b += 1
        return min(a, b)