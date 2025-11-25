# https://leetcode.com/problems/removing-stars-from-a-string/description/
class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for ch in s:
            if stack and ch == '*':
                stack.pop()
            elif ch!='*':
                stack.append(ch)

        return ''.join(stack)
    

    # def removeStars(self, s: str) -> str:
    #     stack = []
    #     for ch in s:
    #         if ch == '*':
    #             if stack:
    #                 stack.pop()
    #         else:
    #             stack.append(ch)
    #     return ''.join(stack)
