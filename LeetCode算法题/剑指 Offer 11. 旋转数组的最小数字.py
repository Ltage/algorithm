# https://leetcode.cn/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof/
class Solution:
    def minArray(self, numbers: List[int]) -> int:
        left = 0
        right = len(numbers) - 1
        while left < right:
            mid = (right - left) // 2 + left
            if numbers[right] > numbers[mid]:
                right = mid
            elif numbers[right] < numbers[mid]:
                left = mid + 1
            else:
                right -= 1
        return numbers[left]