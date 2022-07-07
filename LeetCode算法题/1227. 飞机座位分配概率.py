# https://leetcode.cn/problems/airplane-seat-assignment-probability/
class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        return .5 if n >= 2 else 1.
