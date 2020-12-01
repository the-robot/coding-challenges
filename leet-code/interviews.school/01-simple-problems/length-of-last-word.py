# https://leetcode.com/problems/length-of-last-word/

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        
        # best case : O(n) 1 as last word is not empty.
        # worst case: O(n) will be n because there's many empty spaces behind.
        for i in reversed(s.split(" ")):
            word_length = len(i)
            if word_length != 0:
                count = word_length
                break
    
        return count
