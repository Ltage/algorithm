# https://leetcode.cn/problems/range-module/
class RangeModule:
    N = 1_000_000_000

    # 节点类
    class Range:
        def __init__(self):
            self.leftChild = None
            self.rightChild = None
            self.isLazy = False
            self.isCovered = False

    def __init__(self):
        self.root = self.Range()

    #  任务下发，因为是之前父节点懒住的任务，所以左右节点继续懒住，同时更改区间状态(父节点之前懒住的状态)
    def pushDown(self, node):
        if not node.leftChild:
            node.leftChild = self.Range()
        if not node.rightChild:
            node.rightChild = self.Range()
        if not node.isLazy:
            return

        node.leftChild.isLazy = node.rightChild.isLazy = True
        node.leftChild.isCovered = node.rightChild.isCovered = node.isCovered
        node.isLazy = False  # 下发了所以不懒了

    def pushUp(self, node):
        node.isCovered = node.leftChild.isCovered and node.rightChild.isCovered

    # 更新区间状态，[left, right]为任务区间，[l,r]为当前区间
    def update(self, node, l, r, left, right, covered):

        # 当前节点区间在任务区间内，表明当前节点下的所有节点都会变为同一状态，则在当前节点懒更新
        if left <= l and r <= right:
            node.isLazy = True
            node.isCovered = covered
            return

        # 运行到这说明之前的任务懒不住啦，先将之前懒住的任务下发到左右孩子节点
        self.pushDown(node)

        # 下发完成后，以二分的方式继续更新左右孩子区间
        mid = (r - l) // 2 + l
        if left <= mid:
            self.update(node.leftChild, l, mid, left, right, covered)
        if right > mid:
            self.update(node.rightChild, mid + 1, r, left, right, covered)

        self.pushUp(node)

    # 把各部分的cover状态保存在ans中，返回"and"结果值即可
    def query(self, node, l, r, left, right):
        ans = True
        if left <= l and r <= right:
            return node.isCovered

        # 将要查询的区间节点可能还并不存在，所以要进行创建及下发操作
        self.pushDown(node)

        mid = (r - l) // 2 + l
        if left <= mid:
            ans &= self.query(node.leftChild, l, mid, left, right)
        if right > mid:
            ans &= self.query(node.rightChild, mid + 1, r, left, right)

        return ans

    def addRange(self, left: int, right: int) -> None:
        self.update(self.root, 1, self.N, left, right - 1, True)

    def queryRange(self, left: int, right: int) -> bool:
        return self.query(self.root, 1, self.N, left, right - 1)

    def removeRange(self, left: int, right: int) -> None:
        self.update(self.root, 1, self.N, left, right - 1, False)


# Your RangeModule object will be instantiated and called as such:
obj = RangeModule()
obj.addRange(10, 20)
obj.removeRange(14, 16)
print(obj.queryRange(13, 16))
print(obj.queryRange(13, 15))
print(obj.queryRange(16, 17))
