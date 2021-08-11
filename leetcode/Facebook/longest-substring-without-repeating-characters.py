# https://leetcode.com/problems/longest-substring-without-repeating-characters/

import math

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        N = len(s)
        
        # base case
        if N == 0:
            return 0
        
        seen = {}
        longest_substring = 0
        left = 0
        right = 0
        
        while right < N:
            right_char = s[right]
            seen[right_char] = seen.get(right_char, 0) + 1
            
            while seen[right_char] > 1:
                left_char = s[left]
                seen[left_char] -= 1
                left += 1

            longest_substring = max(longest_substring, right - left + 1)            
            right += 1
        
        return longest_substring
