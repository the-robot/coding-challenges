# https://leetcode.com/problems/find-all-anagrams-in-a-string/

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # get target frequency
        frequency = {}
        for c in p:
            frequency[c] = frequency.get(c, 0) + 1
        
        # string lengths
        S = len(s)
        P = len(p)
        
        # two pointer
        left = 0
        right = 0
        matches = 0
        
        # store anagram starting points
        anagrams = []
        
        while right < S:
            right_char = s[right]
            
            # if inside frequency, decrement the count
            if right_char in frequency:
                frequency[right_char] -= 1
                if frequency[right_char] == 0:
                    matches += 1
            
            # we match the anagram
            if matches == len(frequency):
                anagrams.append(left)
            
            if right >= P - 1:
                left_char = s[left]
                left += 1
                
                if left_char in frequency:
                    if frequency[left_char] == 0:
                        matches -= 1
                    frequency[left_char] += 1
            
            right += 1
        
        return anagrams
