from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # left and right pointer
        left = 0
        right = len(nums) - 1 # to keep track of last non-zero digit

        # while they do not overlap yet
        # means they may be 0 that can be moved to behind
        while left < right:
            if nums[left] == 0:
                del nums[left]
                nums.append(0)
                right -= 1
            else:
                left += 1


solution = Solution()

# Test Cases
case1 = [0, 1, 0, 3, 12]
case2 = [0, 0, 1]

solution.moveZeroes(case1)
assert case1 == [1, 3, 12, 0, 0]

solution.moveZeroes(case2)
assert case2 == [1, 0, 0]
