from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # sort the numbers (or use python built-in 'sorted')
        self.sort(nums)

        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i + 1]:
                return True
            i += 1

        return False

    def sort(self, nums: List[int]):
        """
        Insertion Sort
        """

        length = len(nums)
        i = 1

        while i < length:
            current_position = i

            for j in reversed(range(i)):
                if nums[current_position] < nums[j]:
                    nums[current_position], nums[j] = nums[j], nums[current_position]
                    current_position = j

            i += 1


solution = Solution()

# Test Cases
case1 = [1, 2, 3, 1]
case2 = [1, 2, 3, 4]
case3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]

assert solution.containsDuplicate(case1) == True
assert solution.containsDuplicate(case2) == False
assert solution.containsDuplicate(case3) == True

