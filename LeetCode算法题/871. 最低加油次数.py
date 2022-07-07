# https://leetcode.cn/problems/minimum-number-of-refueling-stops/
# 贪心 + 优先队列
from typing import List


class Solution:
    @staticmethod
    def minRefuelStops(target: int, startFuel: int, stations: List[List[int]]) -> int:
        i = 0
        dis = startFuel
        from queue import PriorityQueue
        pq = PriorityQueue()
        cnt = 0

        while dis < target:
            while i < len(stations) and dis >= stations[i][0]:
                pq.put(-stations[i][1])
                i += 1
            if not pq.qsize():
                return -1
            dis -= pq.get()
            cnt += 1
        return cnt
