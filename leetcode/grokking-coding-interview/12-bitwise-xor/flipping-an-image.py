# https://leetcode.com/problems/flipping-an-image/

from typing import List

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        C = len(image)

        for row in image:
            # traverse only half the column, so we can flip
            for i in range((C + 1) // 2):
                row[i], row[C - i - 1] = row[C - i - 1] ^ 1, row[i] ^ 1
        
        return image
