# https://leetcode.cn/problems/most-stones-removed-with-same-row-or-column/
# 并查集
from typing import List


class DisjointSet:
    def __init__(self):
        self.parent = {}
        self.rank = {}

    def find_ancestor(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 0
        if x == self.parent[x]:
            return x
        x = self.parent[x]
        return self.find_ancestor(x)

    def union_set(self, x, y):
        fx, fy = self.find_ancestor(x), self.find_ancestor(y)
        if fx == fy:
            return
        if self.rank[fx] < self.rank[fy]:
            self.parent[fx] = fy
        elif self.rank[fx] > self.rank[fy]:
            self.parent[fy] = fx
        else:
            self.parent[fx] = fy
            self.rank[fy] += 1

    def count_connected_component(self):
        return sum(i == self.parent[i] for i in self.parent)


class Solution:
    @staticmethod
    def removeStones(stones: List[List[int]]) -> int:
        d = DisjointSet()
        for x, y in stones:
            d.union_set(x, y + 10001)
        return len(stones) - d.count_connected_component()