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
            cnt = 0
            l = 0
            r = 0
            while l < len(nums) - 1:
                if r < len(nums):
                    while nums[r] - nums[l] <= mid:
                        r += 1
                        if r > len(nums) - 1:
                            break
                cnt += r - l - 1
                l += 1
            if cnt < k:
                left = mid + 1
            else:
                right = mid - 1

        return left


print(Solution.smallestDistancePair([62, 100, 4],
                                    2))
