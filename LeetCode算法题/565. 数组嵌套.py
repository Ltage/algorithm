# https://leetcode.cn/problems/array-nesting/
# 将经过的点原地标记，再次走到时不操作
from typing import List


class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        ans = -1
        n = len(nums)
        for i in range(n):
            cnt = 0
            while nums[i] != n:
                cnt += 1
                nums[i], i = n, nums[i]
            ans = max(ans, cnt)
        return ans