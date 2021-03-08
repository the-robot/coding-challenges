# https://leetcode.com/problems/find-k-pairs-with-smallest-sums/

from typing import List
import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        # we use maxHeap so that we can pop largest number among k+1 numbers in maxHeap first
        maxHeap = []

        for x in nums1:
            for y in nums2:
                total = x + y
                heapq.heappush(maxHeap, [-total, [x, y]])

                # pop the largest number among k+1 numbers in maxHeap, so that only
				# k smallest numbers are in maxHeap
                if len(maxHeap) > k:
                    heapq.heappop(maxHeap)

        result = []
        while maxHeap:
            popped = heapq.heappop(maxHeap)
            result.append(popped[1])

        return result
