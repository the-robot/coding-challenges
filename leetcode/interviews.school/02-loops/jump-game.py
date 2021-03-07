# https://leetcode.com/problems/jump-game/

from typing import List

class Solution:
    """Greedy Algorithm"""
    def canJump(self, nums: List[int]) -> bool:
        lastPos = len(nums) - 1
        
        i = len(nums) - 1
        while i >= 0:
            if i + nums[i] >= lastPos:
                lastPos = i

            i -= 1

        return lastPos == 0


class Solution1:
    """Dynamic programming (top-down) solution"""

    def __init__(self):
        self.memo = {}

    def canJumpFromPosition(self, position: int, nums: List[int]) -> bool:
        # edge case
        if position in self.memo:
            return self.memo[position]

        furthestJump = min(position + nums[position], len(nums) - 1)
        nextPosition = furthestJump

        while nextPosition > position:
            if self.canJumpFromPosition(nextPosition, nums):
                self.memo[position] = True
                return True
            nextPosition -= 1

        self.memo[position] = False
        return False

    def canJump(self, nums: List[int]) -> bool:
        self.memo[len(nums) - 1] = True
        return self.canJumpFromPosition(0, nums)


class Solution2:
    """Dynamic programming (bottom-up) solution"""
    def canJump(self, nums: List[int]) -> bool:
        memo = ["U" if i != len(nums)-1 else "G" for i in range(len(nums))]

        i = len(nums) - 2
        while i >= 0:
            furthestJump = min(i + nums[i], len(nums) - 1)

            j = i + 1
            while j <= furthestJump:
                if memo[j] == "G":
                    memo[i] = "G"
                    break
                j += 1

            i -= 1

        return memo[0] == "G"
