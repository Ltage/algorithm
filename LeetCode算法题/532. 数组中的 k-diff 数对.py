# https://leetcode.cn/problems/k-diff-pairs-in-an-array/
from typing import List
import bisect


class Solution:
    @staticmethod
    def findPairs(nums: List[int], k: int) -> int:
        ans = 0
        nums.sort()
        right = len(nums) - 1
        while right > 0:
            rank = bisect.bisect_left(nums, nums[right] - k)
            if rank < right:
                if nums[rank] == nums[right] - k:
                    ans += 1
            right -= 1
            if right == 0:
                return ans
            while nums[right] == nums[right + 1]:
                right -= 1
                if right == 0:
                    return ans

        return ans


print(Solution.findPairs([1, 1], 0))
