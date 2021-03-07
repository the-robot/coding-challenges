# https://leetcode.com/problems/sort-characters-by-frequency/

import heapq

class Solution:
    def frequencySort(self, s: str) -> str:
        charFrequencyMap = {}
        for c in s:
            # we store frequency as negative, -1 for every occurrence
            # because later we can to store in maxheap, most frequent comes first
            charFrequencyMap[c] = charFrequencyMap.get(c, 0) - 1
        
        maxHeap = []
        result = ""
        
         # go through all the numbers of the frequency map and push them in the maxheap
        for char, frequency in charFrequencyMap.items():
            heapq.heappush(maxHeap, (frequency, char))
        
        while maxHeap:
            popped = heapq.heappop(maxHeap)
            result += popped[1] * (popped[0] * -1)
        
        return result
