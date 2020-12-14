# https://leetcode.com/problems/product-of-array-except-self/

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        result = [1]

        # product before
        for i in range(1, length):
            result.append(result[i-1] * nums[i-1])

        # product after
        productAfter = 1
        for i in reversed(range(length)):
            productAfter *= 1 if i == length-1 else nums[i+1]
            result[i] *= productAfter

        return result
