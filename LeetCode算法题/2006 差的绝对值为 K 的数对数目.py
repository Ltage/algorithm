# https://leetcode.cn/problems/count-number-of-pairs-with-absolute-difference-k/
from typing import List


class Solution:
    @staticmethod
    def countKDifference(nums: List[int], k: int) -> int:
        ans = 0
        count_arr = [0] * 100
        for i in range(len(nums)):
            if 0 < nums[i] - k < 100:
                ans += count_arr[nums[i] - k]
            if 0 < nums[i] + k < 100:
                ans += count_arr[nums[i] + k]
            count_arr[nums[i]] += 1
        return ans
