# https://www.educative.io/courses/grokking-the-coding-interview/B1ZW38kXJB2

from typing import List
import math


class ArrayReader:
    def __init__(self, arr: List[int]):
        self.arr = arr

    def get(self, index: int) -> int:
        if index >= len(self.arr):
            return math.inf
        return self.arr[index]
    
    def __len__(self):
        return len(self.arr)


class Solution:
    def search(self, reader: ArrayReader, target:int) -> int:
        return self.binarySearch(reader, target, 0, len(reader) - 1)
    
    def binarySearch(self, reader: ArrayReader, target: int, left: int, right: int) -> int:
        mid = left + (right - left) // 2

        # if mid is the target; return mid because we found the target
        if reader.get(mid) == target:
            return mid

        # if length is 1 and it is not the same as target, the target
        # does not exists; return -1
        if (right - left + 1) == 1 and reader.get(mid) != target:
            return -1

        # search left or right side
        if reader.get(mid) > target:
            return self.binarySearch(reader, target, left, mid)
        else:
            return self.binarySearch(reader, target, mid + 1, right)


if __name__ == "__main__":
    s = Solution()

    reader = ArrayReader([4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30])
    print(s.search(reader, 16))
    print(s.search(reader, 11))

    reader = ArrayReader([1, 3, 8, 10, 15])
    print(s.search(reader, 15))
    print(s.search(reader, 200))
