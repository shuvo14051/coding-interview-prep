Python"""
LeetCode 1598: Crawler Log Folder 
https://leetcode.com/problems/crawler-log-folder/description/?envType=problem-list-v2&envId=stack

Description:
The Leetcode file system keeps a log each time some user performs a change folder operation.
The operations are described below:
- "../" : Move to the parent folder of the current folder. (If you are already in the main folder, remain in the same folder).
- "./" : Remain in the same folder.
- "x/" : Move to the child folder named x (This folder is guaranteed to always exist).
You are given a list of strings logs where logs[i] is the operation performed by the user at the ith step.
The file system starts in the main folder, then the operations in logs are performed.
Return the minimum number of operations needed to go back to the main folder after the change folder operations.

Example 1:
Input: logs = ["d1/","d2/","../","d21/","./"]
Output: 2

Example 2:
Input: logs = ["d1/","d2/","./","d3/","../","d31/"]
Output: 3

Example 3:
Input: logs = ["d1/","../","../","../"]
Output: 0
"""

from typing import List 

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for folder in logs:
            if folder == './':
                continue
            elif folder == '../':
                if stack:
                    stack.pop()
            else:
                stack.append(folder)

        return len(stack)
    
