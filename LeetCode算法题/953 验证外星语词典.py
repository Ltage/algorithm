# https://leetcode.cn/problems/verifying-an-alien-dictionary/


class Solution:
    @staticmethod
    def isAlienSorted(words, order) -> bool:
        i = 0
        while i < len(words) - 1:
            # compare(words[i], words[i + 1])
            minlength = len(words[i]) if len(words[i]) <= len(words[i + 1]) else len(words[i + 1])
            j = 0
            while j <= minlength - 1:
                if order.index(words[i][j]) < order.index(words[i + 1][j]):
                    break
                elif order.index(words[i][j]) == order.index(words[i + 1][j]):
                    j += 1
                    if (j == minlength) & (len(words[i + 1]) < len(words[i])):
                        return False
                else:
                    return False
            i += 1
        return True


words = ["kuvp", "q"]
order = "ngxlkthsjuoqcpavbfdermiywz"

print(Solution.isAlienSorted(words=words, order=order))