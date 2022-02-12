from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map = {}

        for i, num in enumerate(nums):
            pair = target - num
            if pair in index_map:
                return [index_map[pair], i]
            index_map[num] = i

        return None



solution = Solution()

# Test Cases
case1_nums, case1_target = [4, 7, 11, 15], 9

assert solution.twoSum(case1_nums, case1_target) == [0, 1]
