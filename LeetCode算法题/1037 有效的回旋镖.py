# https://leetcode.cn/problems/valid-boomerang/
from typing import List


class Solution:
    @staticmethod
    def isBoomerang(points: List[List[int]]) -> bool:
        return (points[0][0] - points[1][0]) * (points[1][1] - points[2][1]) != (points[0][1] - points[1][1]) * (
                    points[1][0] - points[2][0])
