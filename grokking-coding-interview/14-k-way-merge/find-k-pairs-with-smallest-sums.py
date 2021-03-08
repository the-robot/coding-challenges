# https://leetcode.com/problems/find-k-pairs-with-smallest-sums/

from typing import List
import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        # we use maxHeap so that we can pop largest number among k+1 numbers in maxHeap first
        maxHeap = []

        """
        instead of iterating over all the numbers of both array, we can iterate only
        the first 'K' numbers from both array.

        Since they are sorted in ascending order, the pairs with the minimum sum will
        be just the first 'K' numbers from those two arrays.
        """
        for i in range(0, min(k, len(nums1))):
            for j in range(0, min(k, len(nums2))):
                x = nums1[i]
                y = nums2[j]
                
                total = x + y
                heapq.heappush(maxHeap, [-total, x, y])

                # pop the largest number among k+1 numbers in maxHeap, so that only
				# k smallest numbers are in maxHeap
                if len(maxHeap) > k:
                    heapq.heappop(maxHeap)
                    
        result = []
        while maxHeap:
            popped = heapq.heappop(maxHeap)
            result.append([popped[1], popped[2]])

        return result
