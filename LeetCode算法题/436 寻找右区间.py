# https://leetcode.cn/problems/find-right-interval/
from typing import List
from bisect import bisect_left


class Solution:
    @staticmethod
    def findRightInterval(intervals: List[List[int]]) -> List[int]:
        temp = sorted(intervals)
        res = []
        for i in range(len(intervals)):
            r = bisect_left(temp, [intervals[i][1],])
            if r == len(intervals):
                res.append(-1)
            else:
                res.append(intervals.index(temp[r]))
        print(res)
        return res


Solution.findRightInterval([[16, 17], [1, 12], [2, 9], [3, 10], [13, 14], [15, 16]])
