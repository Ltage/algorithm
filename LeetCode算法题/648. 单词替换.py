# https://leetcode.cn/problems/replace-words/
import bisect
from typing import List


class Solution:
    @staticmethod
    def replaceWords(dictionary: List[str], sentence: str) -> str:
        s = sentence.split()
        dictionary.sort()
        for i, word in enumerate(s):
            min_prefix_length = len(word)
            min_prefix = word
            first_letter = word[0]
            start = bisect.bisect_left(dictionary, first_letter)
            while start < len(dictionary) and dictionary[start][0] == first_letter:
                if min_prefix_length > len(dictionary[start]) and dictionary[start] == word[0:len(dictionary[start])]:
                    min_prefix_length = len(dictionary[start])
                    min_prefix = dictionary[start]
                start += 1
            s[i] = min_prefix
        return " ".join(s)


Solution.replaceWords(["cat", "bat", "rat", "cba"], "the cattle was rattled by the battery")
