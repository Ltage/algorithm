# https://leetcode.cn/problems/queens-that-can-attack-the-king/
# 国王往八个方向走，返回每个方向上碰到的第一个皇后
class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        ans = []
        dir = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]
        for d in dir:
            next_pos = king
            while 0 <= next_pos[0] <= 7 and 0 <= next_pos[1] <= 7:
                if next_pos in queens:
                    ans.append(next_pos)
                    break
                next_pos = [next_pos[i] + d[i] for i in range(len(next_pos))]

        return ans
