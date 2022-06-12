# https://leetcode.cn/problems/remove-outermost-parentheses/
class Solution:
    @staticmethod
    def removeOuterParentheses(s: str) -> str:
        # 方法一
        count = 0
        res = ""
        # "("，")"是成对出现的，count计数每次清零后从新的primitive表达式计数
        for i in s:
            if i == "(":
                count += 1
                if count != 1:  # 不算第一步（在primitive表达式中）
                    res += i
            else:
                count -= 1
                if count != 0:  # 不算最后一步（在primitive表达式中）
                    res += i

        return res

        # 方法二（递归，将string分为未操作和已操作，每次操作第一个primitive表达式）
        # def primitive(string, result):
        #     if (string == "()") or (string == ""):
        #         return result
        #     count = 0
        #     for i in range(len(string)):
        #         if string[i] == "(":
        #             count += 1
        #         else:
        #             count -= 1
        #             if count == 0:
        #                 rest = string[i + 1:]
        #                 result = result + string[1:i]
        #                 return primitive(rest, result)
        # return primitive(s, "")


print(Solution.removeOuterParentheses("(()())(())"))
