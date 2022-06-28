# https://leetcode.cn/problems/random-pick-with-blacklist/
# 前缀和
import bisect
import random
from typing import List


class Solution:

    def __init__(self, n: int, blacklist: List[int]):
        self.blacklist = blacklist
        self.n = n
        if self.blacklist:
            self.res = []
            self.cnt = []
            self.blacklist.append(0)
            self.blacklist.append(self.n)
            self.blacklist.sort()
            i = 1
            if self.blacklist[1] != 0:
                self.res.append((0, self.blacklist[1] - 1))
                self.cnt.append(self.blacklist[1])
            else:
                i = 2
            while i < len(self.blacklist):
                dis = blacklist[i] - blacklist[i - 1]
                if dis > 1:
                    self.res.append((self.blacklist[i - 1] + 1, self.blacklist[i] - 1))
                    self.cnt.append(dis - 1)
                i += 1
            j = 1
            while j < len(self.cnt):
                self.cnt[j] += self.cnt[j - 1]
                j += 1

    def pick(self) -> int:
        if self.blacklist:
            r = random.randint(1, self.cnt[-1])
            rank = bisect.bisect_left(self.cnt, r)
            ans = random.randint(self.res[rank][0], self.res[rank][1])
        else:
            ans = random.randint(0, self.n - 1)
        return ans

# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()