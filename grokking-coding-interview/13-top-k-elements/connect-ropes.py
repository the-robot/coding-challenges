# https://www.educative.io/courses/grokking-the-coding-interview/qVZmZJVxPY0

from typing import List
import heapq

class Solution:
    def connect(self, ropeLengths: List[int]) -> int:
        heapq.heapify(ropeLengths) # change into minheap
        cost = 0

        while len(ropeLengths) > 1:
            # pop first 2 numbers
            a = heapq.heappop(ropeLengths)
            b = heapq.heappop(ropeLengths)

            # connect 2 ropes and add the cost
            ropeSum = a + b
            cost += ropeSum

            # add back the connected rope
            heapq.heappush(ropeLengths, ropeSum)

        return cost

if __name__ == "__main__":
    s = Solution()

    print(s.connect([1, 3, 11, 5]))
    print(s.connect([3, 4, 5, 6]))
    print(s.connect([1, 3, 11, 5, 2]))
