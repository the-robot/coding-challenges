# https://www.educative.io/courses/grokking-the-coding-interview/gx6oKY8PGYY

from typing import List
import heapq


class Solution:
    def findMaxDinstinctElements(self, nums: List[int], k: int) -> int:
        # get frequency of each number
        frequencies = {}
        for num in nums:
            frequencies[num] = frequencies.get(num, 0) + 1

        # add [num, freq] to min heap
        # set num negative, so we can pop larger number first
        maxHeap = []
        for num, freq in frequencies.items():
            heapq.heappush(maxHeap, [-num, freq])

        # pop larger number first, and if it has duplicate and k > 0
        # use k numbers to remove duplicate number
        result = []
        while maxHeap:
            popped = heapq.heappop(maxHeap)

            # if has duplicate and we still have k chances left
            # to use to remove duplicate
            while popped[1] > 1 and k > 0:
                popped[1] -= 1
                k -= 1

            # if no duplicate, add to result; else skip
            if popped[1] == 1:
                result.append(-popped[0])

        # if we still have k, remove some distinct numbers
        # remove the smaller numbers first, so we can get maximum distinct numbers
        while k > 0:
            result = result[:-1]
            k -= 1

        return result

if __name__ == "__main__":
    s = Solution()

    print(s.findMaxDinstinctElements([7, 3, 5, 8, 5, 3, 3], 2))
    print(s.findMaxDinstinctElements([3, 5, 12, 11, 12], 3))
    print(s.findMaxDinstinctElements([1, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5], 2))
