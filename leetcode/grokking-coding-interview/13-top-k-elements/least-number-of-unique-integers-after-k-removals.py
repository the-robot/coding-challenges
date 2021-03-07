# https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/

from typing import List
import heapq

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        # get frequency of each number
        frequencies = {}
        for num in arr:
            frequencies[num] = frequencies.get(num, 0) + 1

        # add [freq, num] to min heap
        # so we can pop least frequent numbers first (unique ones)
        minHeap = []
        for num, freq in frequencies.items():
            heapq.heappush(minHeap, [freq, num])

        # pop less frequent numbers first (uniqes first before duplicate)
        # when we still have k chances
        count = 0
        while minHeap and k > 0:
            popped = heapq.heappop(minHeap)

            # remove all of it's frequencies or up to how many k we have
            canRemove = min(popped[0], k)
            popped[0] -= canRemove
            k -= canRemove
            
            # if we still have frequency > 0; add to result
            if popped[0] > 0:
                count += 1

        # we may still have some numbers in minHeap
        # total count, is the count numbers we counted above after removing some
        # of it's duplicate with k and whatever unique numbers left in minHeap
        return count + len(minHeap)
