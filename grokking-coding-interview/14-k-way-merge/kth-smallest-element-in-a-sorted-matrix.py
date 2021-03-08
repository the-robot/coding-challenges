# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

from typing import List
import heapq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # we use maxHeap so that we can pop largest number among k+1 numbers in maxHeap first
        maxHeap = []
        
        for row in matrix:
            for num in row:
                heapq.heappush(maxHeap, -num)

				# pop the largest number among k+1 numbers in maxHeap, so that only
				# k smallest numbers are in maxHeap
                if len(maxHeap) > k:
                    heapq.heappop(maxHeap)
        
        return -maxHeap[0]
