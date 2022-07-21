# https://leetcode.cn/problems/2-keys-keyboard/
# 分解质因数，求和
class Solution:
    def minSteps(self, n: int) -> int:
        ans = 0
        start = 2
        while start <= n >> 1:
            if n % start == 0:
                ans += start
                n = n // start
                continue
            start += 1
        ans += n
        return ans if n != 1 else 0