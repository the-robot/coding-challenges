# https://leetcode.com/problems/find-peak-element/

from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        return self.binarySearch(nums, 0, len(nums) - 1)
        
    def binarySearch(self, nums: List[int], left: int, right: int) -> int:
        mid = left + (right - left) // 2
        
        # we found the number that is after the ascending
        # but before the descending
        if left == right:
            return left
        
        """
        - if the mid > mid+1 means we are in descending part, so look left
          as the required number is either the mid itself or before mid

        - if the mid <= mid+1 means we are in ascending part, so look right
          as the required number is after mid
        """
        if nums[mid] > nums[mid + 1]:
            return self.binarySearch(nums, left, mid)
        else:
            return self.binarySearch(nums, mid + 1, right)
