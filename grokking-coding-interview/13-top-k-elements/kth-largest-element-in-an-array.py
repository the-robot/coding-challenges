# https://leetcode.com/problems/kth-largest-element-in-an-array/

from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []
        for num in nums:
            heapq.heappush(minHeap, num)
            
            # if greater than k numbers
            # pop the smallest from min heap
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        
        # kth largest element would be first index
        # in min heap of k largest numbers
        return minHeap[0]


class Solution2:
    """ Not recommended as it uses private methods """
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq._heapify_max(nums)
        largestKth = None
        
        i = 0
        while len(nums) > 0 and i < k:
            # if the popped number is kth index, it is the largest
            popped = heapq._heappop_max(nums)
            if i == k - 1:
                largestKth = popped

            i += 1
    
        return largestKth
