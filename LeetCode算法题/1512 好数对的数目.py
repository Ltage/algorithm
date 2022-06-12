# https://leetcode.cn/problems/number-of-good-pairs/
from typing import List


class Solution:
    @staticmethod
    def numIdenticalPairs(nums: List[int]) -> int:
        from collections import Counter
        count = Counter(nums)
        ans = 0
        for i in count:
            if count[i] > 1:
                ans += count[i] * (count[i] - 1) // 2
        return ans


print(Solution.numIdenticalPairs([1, 2, 3, 1, 1, 3]))
