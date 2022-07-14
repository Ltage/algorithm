# https://leetcode.cn/problems/cells-with-odd-values-in-a-matrix/
# 思路:分别统计在横纵坐标中变化奇数次的坐标的个数，计算两个矩形面积，再减去重合部分，因为重合部分变化了（奇数次 + 奇数次）=偶数次
from typing import List


class Solution:
    @staticmethod
    def oddCells(m: int, n: int, indices: List[List[int]]) -> int:
        x = []
        y = []
        for i, j in indices:
            if i in x:
                x.remove(i)
            else:
                x.append(i)
            if j in y:
                y.remove(j)
            else:
                y.append(j)
        return len(x) * n + len(y) * m - 2 * len(x) * len(y)
