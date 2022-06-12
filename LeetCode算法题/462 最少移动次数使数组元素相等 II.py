# https://leetcode.cn/problems/minimum-moves-to-equal-array-elements-ii/
from typing import List


class Solution:
    @staticmethod
    def minMoves2(nums: List[int]) -> int:
        nums = sorted(nums)
        p = nums[len(nums) >> 1]
        step = 0
        for i in nums:
            step += abs(i - p)
        return step


Solution.minMoves2([1, 0, 0, 8, 6])
