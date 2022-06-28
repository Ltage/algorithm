# https://leetcode.cn/problems/longest-uncommon-subsequence-ii/
from collections import defaultdict
from typing import List


class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        ans = -1
        checked = []
        hm = defaultdict(bool)
        for i in strs:
            hm[i] = True
        for i in range(len(strs)):
            if strs[i] in checked:
                continue
            else:
                checked.append(strs[i])
            for j in range(i + 1, len(strs)):
                if strs[i] == strs[j]:
                    hm[strs[i]] = hm[strs[j]] = False
                sub_str = who_is_sub(strs[i], strs[j])
                if sub_str:
                    hm[sub_str] = False
        for i in hm:
            if hm[i]:
                ans = max(ans, len(i))
        return ans



def who_is_sub(str1, str2):
    """
    如果str1是str2的子序列，返回str1
    如果str2是str1的子序列，返回str2
    否则返回False
    """
    m = len(str1)
    n = len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 2)]
    for i in range(n + 1):
        dp[0][i] = 0
    for i in range(m + 1):
        dp[i][0] = 0
    i = 1
    while i <= m:
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] == len(str1):
                    return str1
                if dp[i][j] == len(str2):
                    return str2
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        i += 1
    return False
