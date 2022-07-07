# https://leetcode.cn/problems/my-calendar-i/
class MyCalendar:

    def __init__(self):
        self.L = 0
        self.R = 10 ** 9
        self.tree = set()
        self.lazy = set()

    def insert(self, left, right, start, end, idx):
        if right < start or end < left:
            return

        if start <= left and right <= end:
            self.tree.add(idx)
            self.lazy.add(idx)
            return

        mid = (right - left) // 2 + left
        self.insert(left, mid, start, end, idx * 2)
        self.insert(mid + 1, right, start, end, idx * 2 + 1)
        self.tree.add(idx)
        if idx * 2 in self.lazy and idx * 2 + 1 in self.lazy:
            self.lazy.add(idx)

    def query(self, left, right, start, end, idx):
        if right < start or end < left:
            return False

        if idx in self.lazy:
            return True

        if start <= left and right <= end:
            return idx in self.tree

        mid = (right - left) // 2 + left
        return self.query(left, mid, start, end, idx * 2) or self.query(mid + 1, right, start, end, idx * 2 + 1)

    def book(self, start: int, end: int) -> bool:
        if self.query(self.L, self.R, start, end - 1, 1):
            return False

        self.insert(self.L, self.R, start, end - 1, 1)

        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)

obj = MyCalendar()
print(obj.book(36, 42))
print(obj.book(39, 45))
# print(obj.book(20, 30))
