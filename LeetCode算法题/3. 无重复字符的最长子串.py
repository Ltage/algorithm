#https://leetcode.cn/problems/longest-substring-without-repeating-characters/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hm = {}
        ans = 0
        cnt = 0
        start = 0
        for idx, c in enumerate(s):
            cnt += 1
            if c in hm and hm[c] >= start:  # start之前的值都作废
                cnt = idx - hm[c]
                start = hm[c] + 1
            hm[c] = idx
            ans = max(ans, cnt)
        return ans