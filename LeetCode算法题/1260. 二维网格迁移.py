# https://leetcode.cn/problems/shift-2d-grid/
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        temp = [0] * m * n
        idx = 0
        for i in grid:
            for j in i:
                temp[idx] = j
                idx += 1
        temp = temp[m * n - k % (m * n):] + temp[:m * n - k % (m * n)]
        ans = [[0] * n for _ in range(m)]
        x = 0
        y = 0
        for i in temp:
            ans[x][y] = i
            y += 1
            if y == n:
                x += 1
                y = 0
        return ans