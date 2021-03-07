# https://leetcode.com/problems/find-k-closest-elements/

from typing import List
import heapq

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        minHeap = [] # store [distance, number]
        result = [] # min heap for numbers
        
        # push [dist, num] to minHeap
        for num in arr:
            dist = abs(x - num)
            heapq.heappush(minHeap, [dist, num])

        # add k closest numbers into result
        i = 0
        while minHeap and i < k:
            result.append(heapq.heappop(minHeap)[1])
            i += 1

        # sort the numbers
        result.sort()
        
        return result
