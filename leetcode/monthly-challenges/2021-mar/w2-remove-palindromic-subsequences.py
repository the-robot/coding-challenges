# https://leetcode.com/problems/remove-palindromic-subsequences/

class Solution:
    def removePalindromeSub(self, s: str) -> int:
        # if empty, no steps to make given string empty.
        if not s:
            return 0
    
        # if palindrome, remove the whole string in one step.
        if self.isPalindrome(s):
            return 1
    
        # if not palindrome, remove one palindromic subsequence,
        # and then the remaining.
        return 2

    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False
        
        return True
