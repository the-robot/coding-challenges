# https://www.educative.io/courses/grokking-the-coding-interview/qA5wW7R8ox7

from typing import List

class Solution:
    def ceiling(self, nums: List[int], target: int) -> int:
        # if target is greater than greatest number; return -1
        if target > nums[len(nums) - 1]:
            return -1

        return self.binarySearch(nums, target, 0, len(nums) - 1)

    def binarySearch(self, nums: List[int], target: int, left: int, right: int) -> int:
        # calculate middle number
        middle = int(left + (right - left) / 2)

        # check if middle number is the target, if it is return
        if nums[middle] == target:
            return middle
        
        # if current window size is 1 and it's number is not the target
        # return the middle as mid is the closest greatest
        if (right - left + 1) == 1 and nums[middle] != target:
            return middle

        # check left or right
        if nums[middle] > target:
            return self.binarySearch(nums, target, left, middle)
        else:
            return self.binarySearch(nums, target, middle + 1, right)


if __name__ == "__main__":
    s = Solution()

    print(s.ceiling([4, 6, 10], 6))
    print(s.ceiling([1, 3, 8, 10, 15], 12))
    print(s.ceiling([4, 6, 10], 17))
    print(s.ceiling([4, 6, 10], -1))
