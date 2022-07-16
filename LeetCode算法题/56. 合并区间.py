# https://leetcode.cn/problems/merge-intervals/
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        intervals.sort()
        left = 0
        while left < len(intervals):
            right = left
            p = intervals[left][1]
            while right + 1 < len(intervals) and p >= intervals[right + 1][0]:
                right += 1
                p = max(p, intervals[right][1])
            ans.append([intervals[left][0], p])
            left = right + 1
        return ans

