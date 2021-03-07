# https://leetcode.com/problems/kth-largest-element-in-a-stream/

from typing import List
import heapq

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minHeap = []
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        # add the new number in the min heap
        heapq.heappush(self.minHeap, val)
        
        # if heap has more than 'k' numbers, remove one number
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        
        # return k'th largest number
        return self.minHeap[0]
