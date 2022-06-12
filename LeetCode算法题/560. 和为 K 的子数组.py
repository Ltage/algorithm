# https://leetcode.cn/problems/subarray-sum-equals-k/
from typing import List


class Solution:
    @staticmethod
    def subarraySum(nums: List[int], k: int) -> int:
        hash_map = {0: 1}
        ans = 0
        pre_sum = 0
        for i in nums:
            pre_sum += i
            over_to_k = pre_sum - k
            if over_to_k in hash_map:
                ans += hash_map[over_to_k]
            if pre_sum not in hash_map:
                hash_map[pre_sum] = 1
            else:
                hash_map[pre_sum] += 1

        return ans


print(Solution.subarraySum([1, 1, 1], 2))
