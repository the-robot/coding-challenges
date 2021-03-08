# https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/

from typing import List
import heapq
import math

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        minHeap = []
        rangeStart = 0
        rangeEnd = math.inf

        # max number among first number of each arr
        currentMaxNumber = -math.inf 

        # put the 1st element of each array in the max heap
        for arr in nums:
            heapq.heappush(minHeap, (arr[0], 0, arr))
            currentMaxNumber = max(currentMaxNumber, arr[0])

        """
        take the smallest (top) element from the min heap
        - if it gives us smaller range, update the ranges
        - if the array of the top element has more elements,
          insert the next element in the heap
        """
        while len(minHeap) == len(nums):
            num, i, arr = heapq.heappop(minHeap)

            if rangeEnd - rangeStart > currentMaxNumber - num:
                rangeStart = num
                rangeEnd = currentMaxNumber

            if len(arr) > i + 1:
                # insert the next element in the heap
                heapq.heappush(minHeap, (arr[i+1], i+1, arr))
                currentMaxNumber = max(currentMaxNumber, arr[i+1])

        return [rangeStart, rangeEnd]
