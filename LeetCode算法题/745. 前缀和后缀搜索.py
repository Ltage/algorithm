# https://leetcode.cn/problems/prefix-and-suffix-search/
# 双字典树
from typing import List


class WordFilter:

    def __init__(self, words: List[str]):
        self.words = words
        self.p = {}
        self.s = {}
        for i, word in enumerate(self.words):
            temp1 = self.p
            temp2 = self.s
            for ch in word:
                if ch not in temp1:
                    temp1[ch] = {}
                    temp1[ch]["#"] = [i]
                else:
                    temp1[ch]["#"].append(i)
                temp1 = temp1[ch]

            for ch in word[::-1]:
                if ch not in temp2:
                    temp2[ch] = {}
                    temp2[ch]["#"] = {i}
                else:
                    temp2[ch]["#"].add(i)
                temp2 = temp2[ch]

    def find(self, kw, flag):
        if flag:
            dic = self.p
            kw = kw
        else:
            dic = self.s
            kw = reversed(kw)
        for i in kw:
            try:
                temp = dic[i]
                dic = temp
            except KeyError:
                return None
        return temp["#"]

    def f(self, pref: str, suff: str) -> int:
        pre = self.find(pref, True)  # -> list()
        if not pre:
            return -1
        suf = self.find(suff, False)  # -> set()
        if not suf:
            return -1
        for i in pre[::-1]:
            if i in suf:
                return i
        return -1

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)