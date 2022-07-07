# https://leetcode.cn/problems/sort-characters-by-frequency/
# 计数
from collections import Counter


class Solution:
    @staticmethod
    def frequencySort(s: str) -> str:
        ans = ""
        cnt = Counter(s)
        while cnt:
            c = max(cnt, key=lambda k: cnt[k])
            ans += c * cnt[c]
            del cnt[c]
        return ans