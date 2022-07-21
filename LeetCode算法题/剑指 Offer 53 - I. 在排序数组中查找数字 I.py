# https://leetcode.cn/problems/zai-pai-xu-shu-zu-zhong-cha-zhao-shu-zi-lcof/
class Solution:
    def bs(self, nums, target, higher):
        left = 0
        right = len(nums)
        while left < right:
            mid = (right - left) // 2 + left
            if target < nums[mid] or (not higher and target <= nums[mid]):
                right = mid
            else:
                left = mid + 1
        return left

    def search(self, nums: List[int], target: int) -> int:
        return self.bs(nums, target, True) - self.bs(nums, target, False)