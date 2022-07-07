# https://leetcode.cn/problems/count-items-matching-a-rule/
from typing import List


class Solution:
    @staticmethod
    def countMatches(items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        return sum(i[{"type": 0, "color": 1, "name": 2}[ruleKey]] == ruleValue for i in items)