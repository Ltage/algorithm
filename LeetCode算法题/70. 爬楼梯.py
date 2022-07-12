# https://leetcode.cn/problems/climbing-stairs/
class Solution:
    def climbStairs(self, n: int) -> int:
        a = 1
        b = 2
        if n < 3:
            return n
        for i in range(2, n):
            c = a + b
            a = b
            b = c
        return c