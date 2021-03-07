# https://leetcode.com/problems/reorganize-string/

import heapq

class Solution:
    def reorganizeString(self, S: str) -> str:
        frequencies = {}
        for char in S:
            frequencies[char] = frequencies.get(char, 0) + 1
        
        """
        add all characters to maxHeap, we use maxHeap because
        we should first append the most frequent characters to
        the output string
        """
        maxHeap = []
        for char, freq in frequencies.items():
            heapq.heappush(maxHeap, [-freq, char])

        previousChar = None
        previousFreq = 0
        resultString = []
        
        while maxHeap:
            freq, char = heapq.heappop(maxHeap)
            
            # add the previous entry back in the heap if it's frequency is greater than zero
            if previousChar and -previousFreq > 0:
                heapq.heappush(maxHeap, [previousFreq, previousChar])
            
            # append the current character to the result string and decrement it's count
            resultString.append(char)
            previousChar = char
            previousFreq = freq + 1 # decrement the frequency (freq is neg from maxHeap)
        
        # if not the same length, means cannot be reorganized in such a way that
        # no two same characters come next to each other.
        return "".join(resultString) if len(resultString) == len(S) else ""
