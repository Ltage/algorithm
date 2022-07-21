# https://leetcode.cn/problems/que-shi-de-shu-zi-lcof/
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (right - left) // 2 + left
            if nums[mid] == mid:
                left = mid + 1
            else:
                right = mid - 1
        return left
