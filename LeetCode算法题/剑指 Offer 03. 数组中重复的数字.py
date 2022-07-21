# https://leetcode.cn/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof/
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            while num != i:
                if nums[num] == num:
                    return num
                nums[num], nums[i] = nums[i], nums[num]
                num = nums[i]