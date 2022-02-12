# https://leetcode.com/problems/search-in-rotated-sorted-array/

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                return mid
            
            # left side is sorted in ascending order
            if nums[left] <= nums[mid]:
                if target >= nums[left] and target < nums[mid]:
                    right = mid - 1
                else: # target > nums[mid]
                    left = mid + 1
            # right side is sorted in ascending order
            else:
                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                else: # target < nums[mid]
                    right = mid - 1

        return -1
