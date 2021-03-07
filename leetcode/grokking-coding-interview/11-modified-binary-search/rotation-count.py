# https://www.educative.io/courses/grokking-the-coding-interview/7nPmB8mZ6vj

from typing import List


class Solution:
    def count(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            # if mid is greater than the next element
            if mid < right and nums[mid] > nums[mid + 1]:
                return mid + 1
            
            # if mid is smaller than the previous element
            if mid > left and nums[mid - 1] > nums[mid]:
                return mid
            
            # left side is sorted, so the pivot is on right side
            if nums[left] < nums[mid]:
                left = mid + 1
            # right side is sorted, so the pivot is on left side
            else:
                right = mid - 1
        
        # the array has not been rotated
        return 0


if __name__ == "__main__":
    s = Solution()

    print(s.count([10, 15, 1, 3, 8]))
    print(s.count([4, 5, 7, 9, 10, -1, 2]))
    print(s.count([1, 3, 8, 10]))
