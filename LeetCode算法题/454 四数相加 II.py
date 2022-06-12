# https://leetcode.cn/problems/4sum-ii/
from typing import List
from collections import Counter


class Solution:
    @staticmethod
    def fourSumCount(nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        ans = 0
        n = len(nums1)
        hm = Counter(i + j for i in nums1 for j in nums2)

        for k in nums3:
            for m in nums4:
                if - k - m in hm:
                    ans += hm[- k - m]

        return ans


print(Solution.fourSumCount(nums1=[1, 2], nums2=[-2, -1], nums3=[-1, 2], nums4=[0, 2]))
