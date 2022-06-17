# https://leetcode.cn/problems/duplicate-zeros/
from typing import List


class Solution:
    @staticmethod
    def duplicateZeros(arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        idx = n = len(arr) - 1
        offset = arr.count(0)
        while idx >= 0:
            if idx + offset <= n:
                arr[idx + offset] = arr[idx]

            if arr[idx] == 0:
                offset -= 1
                if idx + offset <= n:
                    arr[idx + offset] = 0
            idx -= 1


Solution.duplicateZeros([0, 0, 4, 0, 3, 0, 2, 0, 1])
