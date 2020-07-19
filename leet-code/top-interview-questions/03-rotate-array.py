from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        i = 0

        while i < k:
            to_shift = nums[-1]

            del nums[-1]
            nums.insert(0, to_shift)

            i += 1


solution = Solution()

# Test Cases
case1_nums, case1_k = [1,2,3,4,5,6,7], 3
case2_nums, case2_k = [-1,-100,3,99], 2

solution.rotate(case1_nums, case1_k)
solution.rotate(case2_nums, case2_k)

assert case1_nums == [5,6,7,1,2,3,4]
assert case2_nums == [3,99,-1,-100]
