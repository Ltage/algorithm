# https://leetcode.cn/problems/count-largest-group/
# 暴力
class Solution:
    def countLargestGroup(self, n: int) -> int:
        cnt = [0] * 37
        for i in range(1, n + 1):
            s = sum(int(i) for i in list(str(i)))
            cnt[s] += 1
        return sum(i == max(cnt) for i in cnt)