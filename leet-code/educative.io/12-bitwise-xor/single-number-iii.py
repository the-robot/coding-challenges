# https://leetcode.com/problems/single-number-iii/

from typing import List

"""
[1, 2, 1, 3, 2, 5]

Since all numbers other than, 3 and 5 got duplicates, if we do XOR of the array
we will get the XOR value of 3 and 5. The rest will be cancelled out.

So according to the above numbers, n1xn2 will become 6, 3 ^ 5 = 6 (110).

As num1 (3) and num2 (5) are different numbers, therefore, they should have at least
one bit different between them.
3 -> 011, 5 -> 101, 6 -> 110

If we know the rightmost bit, we know that any bits before that is the same for num1 and num2.
Rightmost bit is 10.

Using that rightmost bit, we can partition all numbers in the array, into two groups.
    - one group will have all those numbers with that bit set to '0'
    - one group will have all those numbers with that bit set to '1'

This will ensure that num1 will be in one group and num2 will be in another group.
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # get XOR of all the numbers
        n1xn2 = 0
        for num in nums:
            n1xn2 ^= num
        
        # get the rightmost bit that is '1'
        rightmostSetBit = 1
        while (rightmostSetBit & n1xn2) == 0:
            rightmostSetBit = rightmostSetBit << 1

        num1, num2 = 0, 0
        for num in nums:
            if (num & rightmostSetBit) != 0: # the bit is set
                num1 ^= num
            else: # the bit is not set
                num2 ^= num

        return [num1, num2]
