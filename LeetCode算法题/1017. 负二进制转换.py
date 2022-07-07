# https://leetcode.cn/problems/convert-to-base-2/
class Solution:
    def baseNeg2(self, n: int) -> str:
        if n == 0:
            return "0"
        ans = ""
        while n:
            z = n & 1
            ans = str(z) + ans
            n = (z - n) >> 1
        return ans