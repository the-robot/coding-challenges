# https://leetcode.com/problems/kth-largest-element-in-an-array/

from typing import List
import heapq

class Solution:
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
