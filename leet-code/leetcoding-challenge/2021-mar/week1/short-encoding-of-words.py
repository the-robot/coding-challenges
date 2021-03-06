# https://leetcode.com/problems/short-encoding-of-words/

from typing import List

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        """
        we sort by longer string to shorter string
        because longer string is more likely to be included in encoding
        so we want to loop by longer strings first and the string behind can
        look up the longer strings to see if they can be encoded.
        """
        words.sort(key=len, reverse=True)
        
        lookup = set()
        length = 0
        
        for word in words:
            if word in lookup:
                continue
            
            length += len(word) + 1 # +1 for #

            """
            Add the word by reverse to lookup.
            I.e., time -> e, me, ime, time
            
            The reason is encoding is from right to left, cannot be in the middle
            or left to middle. So in total, the word, time can encode the above 4 substrings.
            """
            for x in range(1, len(word) + 1):
                lookup.add(word[-x:])

        return length
