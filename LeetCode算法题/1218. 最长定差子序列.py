# https://leetcode.cn/problems/longest-arithmetic-subsequence-of-given-difference/
class Solution:
    def longestSubsequence(self, arr: List[int], dif: int) -> int:
        hm = {}
        for i in arr:
            if i - dif in hm:
                hm[i] = hm[i - dif] + 1
            else:
                hm[i] = 1
        return max(hm.values())