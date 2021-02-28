# https://leetcode.com/problems/generate-parentheses/

from collections import deque
from typing import List

class ParenthesesString:
    def __init__(self, str, openCount, closeCount):
        self.str = str
        self.openCount = openCount
        self.closeCount = closeCount

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        queue = deque()
        queue.append( ParenthesesString("", 0, 0) )
        
        while queue:
            ps = queue.popleft()
            
            # if we've reached the maximum number of open and close parenthese, add to the result
            if ps.openCount == n and ps.closeCount == n:
                result.append(ps.str)
            else:
                # we can add an open parentheses, add it
                if ps.openCount < n:
                    new = ParenthesesString(
                        str = ps.str + "(",
                        openCount = ps.openCount + 1,
                        closeCount = ps.closeCount,
                    )
                    queue.append(new)
                
                # if we can add a close parentheses, add it
                if ps.openCount > ps.closeCount:
                    new = ParenthesesString(
                        str = ps.str + ")",
                        openCount = ps.openCount,
                        closeCount = ps.closeCount + 1,
                    )
                    queue.append(new)
        
        return result
