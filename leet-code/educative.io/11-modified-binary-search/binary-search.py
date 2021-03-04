# https://leetcode.com/problems/binary-search/

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binarySearch(nums, target, 0, len(nums) - 1)
    
    def binarySearch(self, nums: List[int], target: int, left: int, right: int) -> int:
        # calculate mid number
        mid = int(left + (right - left) / 2)
        
        # check if mid number is the target, if it is return
        if nums[mid] == target:
            return mid
        
        # if current window size is 1 and it's number is not the target
        # means the number does not exists
        if (right - left + 1) == 1 and nums[mid] != target:
            return -1

        # search left or right side
        if nums[mid] > target:
            return self.binarySearch(nums, target, left, mid)
        else:
            return self.binarySearch(nums, target, mid + 1, right)
