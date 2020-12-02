# https://leetcode.com/problems/valid-palindrome/

from typing import List
import re

class Solution:
    def filterAlphanumeric(self, s: str) -> str:
        """
        convert string to lower and filter only alphanumeric characters.
        """
        subPattern = re.compile('[^a-zA-Z0-9]')
        return subPattern.sub('', s.lower())

    def isPalindrome(self, s: str) -> bool:
        s = self.filterAlphanumeric(s)
        length = len(s)

        # only check left-right pointer if length is more than 1
        if length > 1:
            # use pointer to check left-right
            l = 0
            r = length - 1
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
        
        # if not it's true; edge cases for length 0 or 1 is also covered here.
        return True
