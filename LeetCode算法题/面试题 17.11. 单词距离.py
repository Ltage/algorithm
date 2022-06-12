# https://leetcode.cn/problems/find-closest-lcci/
from typing import List


class Solution:
    @staticmethod
    def findClosest(words: List[str], word1: str, word2: str) -> int:
        min_distance = 999999
        # 构建每个单词的索引数组并保存在字典中
        words_idx_map = {}
        # left, right = None, None
        for i in range(len(words)):
            if words[i] not in words_idx_map:
                words_idx_map[words[i]] = [i, ]
            else:
                words_idx_map[words[i]].append(i)

            # if words[i] == word1:
            #     left = i
            # if words[i] == word2:
            #     right = i
            # if (left and right) is not None:
            #     min_distance = min(min_distance, abs(left - right))

        word1_idx = words_idx_map[word1]
        word2_idx = words_idx_map[word2]

        # 二分查找最小值
        def temp_min(num, arr):
            left = 0
            right = len(arr) - 1

            if num < arr[left]:
                return arr[left] - num
            if num > arr[right]:
                return num - arr[right]

            def temp_min_inner(p, a, l, r):
                while l < r:
                    mid = (r - l) // 2 + l
                    if p > a[mid]:
                        return temp_min_inner(p, a, mid + 1, r)
                    else:
                        return temp_min_inner(p, a, l, mid)

                return min(a[l] - p, p - a[l - 1])

            return temp_min_inner(num, arr, left, right)

        # 遍历word1中每个idx找出最小距离

        for i in range(len(word1_idx)):
            min_distance = min(temp_min(word1_idx[i], word2_idx), min_distance)

        return min_distance


Solution.findClosest(["I", "am", "a", "student", "from", "a", "university", "in", "a", "city"], word1="a",
                     word2="student")
