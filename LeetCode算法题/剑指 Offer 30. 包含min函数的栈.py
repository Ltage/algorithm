# https://leetcode.cn/problems/bao-han-minhan-shu-de-zhan-lcof/
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s = []
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.s:
            self.s.append(x)
        else:
            if x <= self.s[-1]:
                self.s.append(x)

    def pop(self) -> None:
        num = self.stack.pop()
        if num == self.s[-1]:
            self.s.pop()

    def top(self) -> int:
        return self.stack[-1]

    def min(self) -> int:
        return self.s[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()
