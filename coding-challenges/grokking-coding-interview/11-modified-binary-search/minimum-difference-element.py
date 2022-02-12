# https://www.educative.io/courses/grokking-the-coding-interview/mymvP915LY9

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        # edge cases
        if target < nums[0]:
            return nums[0]
        elif target > nums[n - 1]:
            return nums[n - 1]

        return self.binarySearch(nums, target, 0, n - 1)

    def binarySearch(self, nums: List[int], target: int, left: int, right: int) -> int:
        # when the element does not exists in the array; we will reach here
        # then chose the closest number, either left or right
        if left > right:
            return nums[left] if (nums[left] - target) < (nums[right] - target) else nums[right]

        mid = left + (right - left) // 2

        if nums[mid] > target:
            return self.binarySearch(nums, target, left, mid - 1)
        elif nums[mid] < target:
            return self.binarySearch(nums, target, mid + 1, right)
        else:
            return nums[mid]

if __name__ == "__main__":
    s = Solution()

    print(s.search([4, 6, 10], 7))
    print(s.search([4, 6, 10], 4))
    print(s.search([1, 3, 8, 10, 15], 12))
    print(s.search([4, 6, 10], 17))
