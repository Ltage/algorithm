# https://leetcode.cn/problems/next-greater-element-iii/
class Solution:
    @staticmethod
    def nextGreaterElement(n: int) -> int:
        t = list(str(n))
        if len(t) == 1:
            return -1
        hi = len(t) - 2
        while hi >= 0:
            if t[hi:] != sorted(t[hi:], reverse=True):
                lo = hi + 1
                while lo < len(t) and t[lo] > t[hi]:
                    lo += 1
                lo -= 1
                t[lo], t[hi] = t[hi], t[lo]
                ans = int("".join(t[:hi + 1] + sorted(t[hi + 1:])))
                return ans if ans.bit_length() < 32 else -1
            hi -= 1
        return -1