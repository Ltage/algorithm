# https://leetcode.cn/problems/wiggle-sort-ii/
from typing import List


class Solution:
    @staticmethod
    def wiggleSort(nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        arr = sorted(nums)
        N = len(nums)
        idx = 0
        left = 0
        right = N - 1
        mid = (right - left) // 2
        flag = True
        while idx < N:
            if flag:
                nums[idx] = arr[mid]
                mid -= 1
                flag = False
            else:
                nums[idx] = arr[right]
                right -= 1
                flag = True
            idx += 1