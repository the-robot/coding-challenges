# https://leetcode.com/problems/kth-largest-element-in-an-array/

from typing import List
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        Calculate euclidean distance and store in * -1, so that we can reverse the heap.
        Python default heap is minheap so by multiplying with -1 we store as maxheap.
        
        We only store k minimum distances and pop any extras.
        """
        maxheap = [] # store {distance, point} pair in maxheap
        result = []

        # calculate distances and add into maxheap
        for point in points:
            # correct euclidean distance formula is sqrt((x2 - x1)^2 + (y2 - y1)^2)
            # in this case, no point sqrt since we do not really care about actual distance.
            # also * -1 so that we pop largest distances first.
            distance = ((point[0] * point[0]) + (point[1] * point[1])) * -1
            heapq.heappush(maxheap, [distance, point])

            # pop any distances larger than k
            if len(maxheap) > k:
                heapq.heappop(maxheap)

        # get first k closest points
        while len(maxheap) > 0:
            popped = heapq.heappop(maxheap)
            result.append(popped[1])

        return result
