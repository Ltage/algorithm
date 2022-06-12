# https://leetcode.cn/problems/find-and-replace-pattern/
from collections import defaultdict
from typing import List


class Solution:
    @staticmethod
    def findAndReplacePattern(words: List[str], pattern: str) -> List[str]:
        ans = []
        for word in words:
            if len(word) != len(pattern):
                continue
            check_w = defaultdict(str)
            check_p = defaultdict(str)
            for i in range(len(pattern)):
                if check_w[word[i]] == "":
                    check_w[word[i]] = pattern[i]
                    if check_p[pattern[i]] == "":
                        check_p[pattern[i]] = word[i]
                    else:
                        if check_p[pattern[i]] != word[i]:
                            break
                else:
                    if check_p[pattern[i]] == "" or check_p[pattern[i]] != word[i]:
                        break
            else:
                ans.append(word)
        return ans


print(Solution.findAndReplacePattern(words=["dkd"], pattern="abb"))
