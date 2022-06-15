# https://leetcode.cn/problems/find-k-th-smallest-pair-distance/
from typing import List
import bisect


class Solution:
    @staticmethod
    def smallestDistancePair(nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        right = nums[-1] - nums[0]
        while left <= right:
            mid = (right - left) // 2 + left
            idx = len(nums) - 1
            cnt = 0
            while idx > 0:
                rank = bisect.bisect_left(nums, nums[idx] - mid)
                if rank < idx:
                    cnt += idx - rank
                idx -= 1
            if cnt < k:
                left = mid + 1
            else:
                right = mid - 1

        return left


print(Solution.smallestDistancePair([1, 7, 10, 15, 15], 3))
