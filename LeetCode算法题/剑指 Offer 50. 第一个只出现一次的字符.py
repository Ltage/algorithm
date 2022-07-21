# https://leetcode.cn/problems/di-yi-ge-zhi-chu-xian-yi-ci-de-zi-fu-lcof/
class Solution:
    def firstUniqChar(self, s: str) -> str:
        hm = Counter(s)
        for i in s:
            if hm[i] == 1:
                return i
        return " "