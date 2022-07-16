# https://leetcode.cn/problems/qIsx9U/
# 队列，动态维护sum值
class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.s = []
        self.total = 0

    def next(self, val: int) -> float:
        self.total += val
        self.s.append(val)
        if len(self.s) > self.size:
            self.total -= self.s.pop(0)
        return self.total / len(self.s)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
