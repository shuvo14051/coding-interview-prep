"""
LeetCode 844: Backspace String Compare
https://leetcode.com/problems/backspace-string-compare/description/

Description:
Given two strings s and t, return true if they are equal when both are typed into empty text editors.
'#' means a backspace character. Note that after backspacing an empty text, the text will continue empty.

Example 1:
Input: s = "ab#c", t = "ad#c"
Output: true

Example 2:
Input: s = "ab##", t = "c#d#"
Output: true

Example 3:
Input: s = "a#c", t = "b"
Output: false
"""

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_s = []
        stack_t = []

        for ch in s:
            if ch == "#":
                if stack_s:
                    stack_s.pop()
            else:
                stack_s.append(ch)

        for ch in t:
            if ch == "#":
                if stack_t:
                    stack_t.pop()
            else:
                stack_t.append(ch)

        return ''.join(stack_s) == ''.join(stack_t)
