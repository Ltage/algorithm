# https://leetcode.cn/problems/max-sum-of-rectangle-no-larger-than-k/
from bisect import bisect_left
from math import inf
from typing import List

from sortedcontainers import SortedList


class Solution:
    @staticmethod
    def maxSumSubmatrix(matrix: List[List[int]], k: int) -> int:
        from sortedcontainers import SortedList
        m = len(matrix)
        n = len(matrix[0])
        ans = -inf
        for start in range(m):
            line = [0] * n
            for end in range(start, m):
                for i in range(n):
                    line[i] += matrix[end][i]
                sorted_line = SortedList([0])
                s = 0
                for num in line:
                    s += num
                    r = bisect_left(sorted_line, s - k)
                    if r != len(sorted_line):
                        ans = max(ans, s - sorted_line[r])
                    sorted_line.add(s)

        return ans


print(Solution.maxSumSubmatrix(matrix=[[2, 2, -1]], k=3))
