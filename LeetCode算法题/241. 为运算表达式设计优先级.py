# https://leetcode.cn/problems/different-ways-to-add-parentheses/
# 分治 + 递归
from typing import List


class Solution:

    def diffWaysToCompute(self, expression: str) -> List[int]:
        ans = []
        if len(expression) < 3:
            ans.append(int(expression))

        for i in range(len(expression)):
            if expression[i] in "+-*":
                left = self.diffWaysToCompute(expression[: i])
                right = self.diffWaysToCompute(expression[i + 1:])
                for l in left:
                    for r in right:
                        if expression[i] == "+":
                            ans.append(l + r)
                        if expression[i] == "-":
                            ans.append(l - r)
                        if expression[i] == "*":
                            ans.append(l * r)
        return ans
