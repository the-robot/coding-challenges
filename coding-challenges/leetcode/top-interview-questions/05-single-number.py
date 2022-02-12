from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        single = nums[0]

        for i in nums[1:]:
            single ^= i

        return single


solution = Solution()

# Test Cases
case1 = [2, 2, 1]
case2 = [4, 1, 2, 1, 2]

assert solution.singleNumber(case1) == 1
assert solution.singleNumber(case2) == 4
