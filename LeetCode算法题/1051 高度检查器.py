# https://leetcode.cn/problems/height-checker/
from typing import List


class Solution:
    @staticmethod
    def heightChecker(heights: List[int]) -> int:
        m = max(heights)
        ans = 0
        cnt = [0] * (m + 1)
        for i in heights:
            cnt[i] += 1
        idx = 0
        for j in range(1, len(cnt)):
            if cnt[j] == 0:
                continue
            for n in range(cnt[j]):
                if heights[idx] != j:
                    ans += 1
                idx += 1
        return ans


print(Solution.heightChecker([1, 1, 4, 2, 1, 3]))
