# https://leetcode.cn/problems/recursive-mulitply-lcci/
class Solution:
    def multiply(self, A: int, B: int) -> int:
        if B == 1:
            return A
        if B & 1:
            return self.multiply(A, B >> 1) + self.multiply(A, B >> 1) + A
        else:
            return self.multiply(A, B >> 1) + self.multiply(A, B >> 1)