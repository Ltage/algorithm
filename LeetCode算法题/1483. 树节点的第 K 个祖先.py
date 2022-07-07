# https://leetcode.cn/problems/kth-ancestor-of-a-tree-node/
# dp倍增
class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        self.dp = [[] for _ in range(n)]
        for i in range(n):
            self.dp[i].append(parent[i])
        for i in range(n):
            j = 1
            while self.dp[i][j - 1] != -1:
                if j > len(self.dp[self.dp[i][j - 1]]):
                    self.dp[i].append(-1)
                    break
                self.dp[i].append(self.dp[self.dp[i][j - 1]][j - 1])
                j += 1

        print(self.dp)

    def getKthAncestor(self, node: int, k: int) -> int:
        ans = node
        pos = 0
        while k:
            if k & 1 and ans != -1:
                if pos >= len(self.dp[ans]):
                    return -1
                ans = self.dp[ans][pos]
            pos += 1
            k >>= 1
        return ans

# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)