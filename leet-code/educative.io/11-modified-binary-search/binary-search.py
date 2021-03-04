# https://leetcode.com/problems/binary-search/

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binarySearch(nums, target, 0, len(nums) - 1)
    
    def binarySearch(self, nums: List[int], target: int, left: int, right: int) -> int:
        # calculate middle number
        middle = int(left + (right - left) / 2)
        
        # check if middle number is the target, if it is return
        if nums[middle] == target:
            return middle
        
        # if current window size is 1 and it's number is not the target
        # means the number does not exists
        if (right - left + 1) == 1 and nums[middle] != target:
            return -1

        # search left or right side
        if nums[middle] > target:
            return self.binarySearch(nums, target, left, middle)
        else:
            return self.binarySearch(nums, target, middle + 1, right)
