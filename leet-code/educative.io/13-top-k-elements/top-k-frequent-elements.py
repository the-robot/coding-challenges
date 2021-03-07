# https://leetcode.com/problems/top-k-frequent-elements/

from typing import List
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numFrequencyMap = {}
        for num in nums:
            numFrequencyMap[num] = numFrequencyMap.get(num, 0) + 1
        
        minHeap = []
        topK = []
        
        # go through all the numbers of the frequency map and push them in the minheap
        # which will be top k frequenct numbers.
        # if the heap size is more than k, we remove the smallest (top) number
        for num, frequency in numFrequencyMap.items():
            heapq.heappush(minHeap, (frequency, num))
            
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        
        # get top K most frequent numbers
        while minHeap:
            popped = heapq.heappop(minHeap)
            topK.append(popped[1])
        
        return topK
