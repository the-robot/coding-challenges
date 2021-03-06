# https://leetcode.com/problems/complement-of-base-10-integer/

class Solution:
    def bitwiseComplement(self, N: int) -> int:
        # edge case, if just one bit and its 0, return 1
        if N == 0 or N == 1:
            return N ^ 1

        # count total number of bit
        bitCount, n = 0, N
        while n > 0:
            bitCount += 1
            n = n >> 1

        allBitsSet = pow(2, bitCount) - 1
        return N ^ allBitsSet
