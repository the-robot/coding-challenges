# https://leetcode.com/problems/palindromic-substrings/

from typing import List

class Solution(object):
    def countSubstrings(self, s: str) -> int:
        palindromics = 0
        n = len(s)
        # edge case; if string is empty no palindromic substrings
        if n == 0:
            return 0

        """
        I.e. if string is "aba"
        n = 3

        i = 0
        left = -1
        right = 1
            - +=1 from for loop
            - not from first while loop (because ab is not palindromic, while i = 0; right = 1)
            - not from second while loop (because left is not >= 0)

        i = 1
        left = 0
        right = 2
            - +=1 from for loop
            - not from first while loop (because ba is not palindromic, while i = 1; right = 2)
            - +=1 from second while loop (because aba is also palindromic, while i = 1; left = 0; right = 2)

        i = 2
        left = 1
        right = 3
            - +=1 from for loop
            - not from first while loop (because right is not < n)
            - not from second while loop (because right is not < n)
        """

        for i in range(n):
            # every word is palindromic substring
            palindromics += 1
            
            left = i - 1
            right = i + 1

            # this is to check if the next word is same as the current word
            while right < n and s[right] == s[i]:
                # if the next one (on right) is the same as current one
                # it is palindromic
                palindromics += 1
                right += 1

            # this is to check if the previous word is same as the next word (mirror)
            # for example when string is aba and current index (i) is 1
            while left >= 0 and right < n and s[left] == s[right]:
                # if the previous one (on left) is the same as current one
                # it is palindromic
                palindromics += 1
                left -= 1
                right += 1

        return palindromics

s = Solution()
s.countSubstrings("aba")
