# https://leetcode.cn/problems/kth-smallest-number-in-multiplication-table/
class Solution:
    @staticmethod
    def findKthNumber(m: int, n: int, k: int) -> int:
        left = 1
        right = m * n
        while left < right:
            mid = ((right - left) >> 1) + left
            # mid为第t小的数
            t = 0
            start = mid // n
            t += start * n
            for i in range(start + 1, m + 1):
                t += mid // i
            if t < k:
                left = mid + 1
            else:
                right = mid
        return left


Solution.findKthNumber(3, 3, 5)
