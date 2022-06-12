# https://leetcode.cn/problems/binary-subarrays-with-sum/
from typing import List


class Solution:
    @staticmethod
    def numSubarraysWithSum(nums: List[int], goal: int) -> int:
        ans = 0
        hash_map = [0] * 60001
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        hash_map[goal] = 1
        for i in range(len(nums)):
            ans += hash_map[nums[i]]
            hash_map[nums[i] + goal] += 1
        return ans


print(Solution.numSubarraysWithSum([0, 1, 0, 0, 0, 0], 0))
