# https://leetcode.cn/problems/random-point-in-non-overlapping-rectangles/
from typing import List
import random
import bisect


class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects

        # 前缀和
        self.pre_area = [0] * len(self.rects)
        self.pre_area[0] = self.area(self.rects[0])
        for i in range(1, len(self.rects)):
            self.pre_area[i] = self.pre_area[i - 1] + self.area(self.rects[i])

    # area为矩形所包含点的数量
    @staticmethod
    def area(rect):
        return (rect[3] - rect[1] + 1) * (rect[2] - rect[0] + 1)

    def pick(self) -> List[int]:
        r = random.randint(1, self.pre_area[-1])
        rect = self.rects[bisect.bisect_left(self.pre_area, r)]
        r_x = random.randint(rect[0], rect[2])
        r_y = random.randint(rect[1], rect[3])
        return [r_x, r_y]


obj = Solution([
    [-2, -2, 1, 1],
    [2, 2, 4, 6]
])
param_1 = obj.pick()
