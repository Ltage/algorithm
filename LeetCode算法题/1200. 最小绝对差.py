# https://leetcode.cn/problems/minimum-absolute-difference/
# 排序 + 遍历
from math import inf
from typing import List


class Solution:
    @staticmethod
    def minimumAbsDifference(arr: List[int]) -> List[List[int]]:
        diff = inf
        res = []
        arr.sort()
        i = 1
        while i < len(arr):
            tmp = arr[i] - arr[i - 1]

            if diff == tmp:
                res.append([arr[i - 1], arr[i]])

            if diff > tmp:
                diff = tmp
                res = [[arr[i - 1], arr[i]]]

            i += 1
        return res