# https://leetcode.cn/problems/asteroid-collision/
# 模拟栈
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in asteroids:
            if not stack:
                stack.append(i)
                continue
            if stack[-1] < 0 or (stack[-1] > 0 and i > 0):
                stack.append(i)
            while stack[-1] > 0 > i:
                if stack[-1] + i == 0:
                    stack.pop()
                    break
                elif stack[-1] + i < 0:
                    stack.pop()
                    if not stack or stack[-1] < 0:
                        stack.append(i)
                        break
                else:
                    break

        return stack
