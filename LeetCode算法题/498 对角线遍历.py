# https://leetcode.cn/problems/diagonal-traverse/
from typing import List


class Solution:
    @staticmethod
    def findDiagonalOrder(mat: List[List[int]]) -> List[int]:
        width = len(mat[0]) - 1
        depth = len(mat) - 1
        ans = []
        flag = 1
        x = y = 0
        while x <= width or y <= depth:
            if x == width and y == depth:
                ans.append(mat[y][x])
                break
            if flag:
                if x > width or y < 0:
                    flag = 0
                    if x > width:
                        x = width
                        if y == -1:
                            y = 1
                        else:
                            y += 2
                        continue
                    if y < 0:
                        y = 0
                        continue
                ans.append(mat[y][x])
                x += 1
                y -= 1
            else:
                if x < 0 or y > depth:
                    flag = 1
                    if y > depth:
                        y = depth
                        if x == -1:
                            x = 1
                        else:
                            x += 2
                        continue
                    if x < 0:
                        x = 0
                        continue
                ans.append(mat[y][x])
                x -= 1
                y += 1
        return ans


print(Solution.findDiagonalOrder([[2, 5], [8, 4], [0, -1]]))
