# https://leetcode.com/problems/pascals-triangle/

from typing import List

class Solution:
    def getValue(self, previousRow: List[int], index: int) -> int:
        left = 0 if index - 1 < 0 else previousRow[index - 1]
        right = 0 if index >= len(previousRow) else previousRow[index]
        return left + right

    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []

        for row in range(numRows + 1):
            # create new row at the bottom
            triangle.append([])

            # create column for the row
            for col in range(row + 1):
                # if it is first row; no parent to look up to
                # so just add 1
                if row == 0:
                    triangle[-1].append(1)
                
                # if not; get value from previous row
                # (index - 1) + (index)
                else:
                    value = self.getValue(triangle[-2], col)
                    triangle[-1].append(value)

        return triangle
