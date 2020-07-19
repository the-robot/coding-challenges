from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        i, j = 0, 1

        while j < length:
            if nums[i] == nums[j]:
                del nums[i]
                length -= 1
            else:
                i += 1
                j += 1

        return length


solution = Solution()

# Test Cases
case1 = [1,1,2]
case2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

assert solution.removeDuplicates(case1) == 2
assert solution.removeDuplicates(case2) == 5
