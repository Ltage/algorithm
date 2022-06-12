# https://leetcode.cn/problems/my-calendar-iii/
from collections import defaultdict


class MyCalendarThree:

    def __init__(self):
        self.tree = defaultdict(int)
        self.lazy = defaultdict(int)

    def insert(self, start, end, left, right, node):
        if right < start or left > end:
            return
        if start <= left and right <= end:
            self.tree[node] += 1
            self.lazy[node] += 1
            return
        mid = (right - left) // 2 + left
        node_left = 2 * node + 1
        node_right = 2 * node + 2
        self.insert(start, end, left, mid, node_left)
        self.insert(start, end, mid + 1, right, node_right)
        self.tree[node] = self.lazy[node] + max(self.tree[node_left], self.tree[node_right])

    def book(self, start: int, end: int) -> int:
        self.insert(start, end - 1, 0, 10 ** 9, 0)
        print(self.tree[0])
        return self.tree[0]


# Your MyCalendarThree object will be instantiated and called as such:
obj = MyCalendarThree()
param_1 = obj.book(1, 2)
param_2 = obj.book(1, 2)
param_3 = obj.book(5, 6)
