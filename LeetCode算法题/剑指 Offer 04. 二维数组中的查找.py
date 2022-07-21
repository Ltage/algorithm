# https://leetcode.cn/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof/
# 四分
class Solution:
    def bs(self, matrix, target, x1, y1, x2, y2):
        if x1 > x2 or y1 > y2:
            return False
        if matrix[x1][y1] == matrix[x2][y2]:
            if matrix[x1][y1] == target:
                return True
            else:
                return False
        mid_x = (x2 - x1) // 2 + x1
        mid_y = (y2 - y1) // 2 + y1
        if matrix[mid_x][mid_y] == target:
            return True
        elif matrix[mid_x][mid_y] < target:
            return self.bs(matrix, target, x1, mid_y + 1, mid_x, y2) or self.bs(matrix, target, mid_x + 1, mid_y + 1, x2, y2) or self.bs(matrix, target, mid_x + 1, y1, x2, mid_y)
        else:
            return self.bs(matrix, target, x1, y1, mid_x - 1, mid_y - 1) or self.bs(matrix, target, x1, mid_y, mid_x - 1, y2) or self.bs(matrix, target, mid_x, y1, x2, mid_y - 1)

    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or matrix == [[]]:
            return False
        m = len(matrix) - 1
        n = len(matrix[0]) - 1
        return self.bs(matrix, target, 0, 0, m, n)
