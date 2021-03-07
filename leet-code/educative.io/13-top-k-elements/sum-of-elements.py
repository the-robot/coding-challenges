# https://www.educative.io/courses/grokking-the-coding-interview/qVljv3Plr67

from typing import List
import heapq


class Solution:
    def sum(self, nums: List[int], k1: int, k2: int) -> int:
        heapq.heapify(nums) # change into minheap
        i = 0
        total = 0

        """
        We need to get numbers between smallest k1'th (exclusive) and smallest k2'th (exclusive).

        If nums = [1, 3, 5, 11, 12, 15], k1 = 3 and k2 = 6 means
        5 (index 2) is 3th smallest number and 15 (index 5) is 6th smallest number.

        By summing numbers between k1 and k2 means, we need to sum when index > 2 and index < 5
        """
        while nums and i < k2 - 1:
            popped = heapq.heappop(nums)

            # if index >= k1 because when k1 = 3th smallest number means
            # in sorted array, it means any indices beyond index 2.
            if i > k1 - 1:
                total += popped
            
            i += 1

        return total


if __name__ == "__main__":
    s = Solution()

    print(s.sum([1, 3, 12, 5, 15, 11], 3, 6))
    print(s.sum([3, 5, 8, 7], 1, 4))
