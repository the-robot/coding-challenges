from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1

        while i >= 0:
            digits[i] = digits[i] + 1

            # if it's 10, change to 0 and add one to next
            if digits[i] == 10:
                digits[i] = 0

                # if it is the first-index, add 1 from head
                if i == 0:
                    digits.insert(0, 1)

                i -= 1
            else:
                break

        return digits


solution = Solution()

# Test Cases
case1 = [1, 2, 3]
case2 = [4, 3, 2, 1]
case3 = [9]

assert solution.plusOne(case1) == [1, 2, 4]
assert solution.plusOne(case2) == [4, 3, 2, 2]
assert solution.plusOne(case3) == [1, 0]
