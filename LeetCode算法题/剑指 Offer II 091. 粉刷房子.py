# https://leetcode.cn/problems/JEj789/
from typing import List


class Solution:
    @staticmethod
    def minCost(costs: List[List[int]]) -> int:
        n = len(costs)
        dp = [[0] * 3 for _ in range(2)]
        for i in range(n):
            for j in range(3):
                dp[i & 1][j % 3] = min(dp[(i - 1) & 1][(j + 1) % 3], dp[(i - 1) & 1][(j + 2) % 3]) + costs[i][j % 3]
        return min(dp[(n - 1) & 1][0], dp[(n - 1) & 1][1], dp[(n - 1) & 1][2])
