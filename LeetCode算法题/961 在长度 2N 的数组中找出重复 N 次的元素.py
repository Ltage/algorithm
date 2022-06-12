# https://leetcode.cn/problems/n-repeated-element-in-size-2n-array/
from typing import List


class Solution:
    @staticmethod
    def repeatedNTimes(nums: List[int]) -> int:
        count = {}
        for i in nums:
            if i not in count:
                count[i] = 1
            else:
                count[i] += 1
                if count[i] == len(nums) / 2:
                    return i


Solution.repeatedNTimes([1, 2, 3, 3])
