# https://leetcode.cn/problems/two-sum/
# 梦开始的地方！
from typing import List


class Solution:
    @staticmethod
    def twoSum(nums: List[int], target: int) -> List[int]:
        hm = {}
        for i in range(len(nums)):
            if nums[i] in hm:
                return [hm[nums[i]], i]
            else:
                hm[target - nums[i]] = i