# https://leetcode.cn/problems/consecutive-numbers-sum/
class Solution:
    @staticmethod
    def consecutiveNumbersSum(k: int) -> int:
        if k == 1:
            return 1
        n = (k + 1) // 2
        ans = 1

        def binary(left, right):
            l = left
            r = right
            while l < r:
                t = (r - l) // 2 + l
                if (n + n * n) // 2 - (t + t * t) // 2 == k:
                    return 1
                elif (n + n * n) // 2 - (t + t * t) // 2 < k:

                    return binary(left, t)
                else:
                    return binary(t + 1, right)
            return 0

        while n > 0:
            left = 0
            right = n
            ans += binary(left, right)
            n -= 1
        return ans


print(Solution.consecutiveNumbersSum(83234))
