# https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/

from typing import List
import heapq
import math

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        """
        First you put all into minHeap, so numbers are sorted from
        smallest first number -> largest first number.

        I.e. [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]] -> [[0,9,12,20],[4,10,15,24,26],[5,18,22,30]]

        In the meantime, you also need to store the largest among the first of each 3 nums. The reason
        is from 0 (start as default) to that max (5 in this case), is a range (0-5) that includes at least
        one number from each of the k lists.

        From that, what we need to do is, increment the `start` while decrementing the `end` and get a smallest
        range that includes at least number one from each k list.
        """

        minHeap = [] # {first number of array, index, [int]}

        # max number among first number of each arr
        currentMaxNumber = -math.inf 

        # put the 1st element of each array in the max heap
        for arr in nums:
            heapq.heappush(minHeap, (arr[0], 0, arr))
            currentMaxNumber = max(currentMaxNumber, arr[0])

        # Smallest range that includes at least one number from each
        # of the k lists. Default is 0 to inf.
        rangeStart = 0
        rangeEnd = math.inf

        """
        take the smallest (top) element from the min heap
        - if it gives us smaller range, update the ranges
        - if the array of the top element has more elements,
          insert the next element in the heap

        currentMaxNumber here is to keep track of next max number.
        Because in every iteration, the start will rangeStart increasing. Therefore,
        we also need to expand the rangeEnd so that overall range still covers all k lists.
        """
        while len(minHeap) == len(nums):
            num, i, arr = heapq.heappop(minHeap)

            # if we find a smaller range, replace that to range start-end
            if rangeEnd - rangeStart > currentMaxNumber - num:
                rangeStart = num
                rangeEnd = currentMaxNumber

            if len(arr) > i + 1:
                # insert the next element in the heap
                heapq.heappush(minHeap, (arr[i+1], i+1, arr))
                currentMaxNumber = max(currentMaxNumber, arr[i+1])

        return [rangeStart, rangeEnd]
