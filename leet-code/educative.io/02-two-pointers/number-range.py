# https://www.educative.io/courses/grokking-the-coding-interview/R1B78K9oBEz

from typing import List

class Solution:
    def findRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1

        while left <= right:
            if nums[left] < target:
                left += 1
            elif nums[right] > target:
                right -= 1
            else:
                return [left, right]

        return [-1, -1]


if __name__ == "__main__":
    s = Solution()

    print(s.findRange([4, 6, 6, 6, 9], 6))
    print(s.findRange([4, 3, 8, 10, 15], 10))
    print(s.findRange([1, 3, 8, 10, 15], 12))
