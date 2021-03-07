# https://leetcode.com/problems/rectangle-overlap/

from typing import List

class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        # find largest x from smallest x position of each rectangle
        left = max(rec1[0], rec2[0])
        
        # find smallest x from largest x position of each rectangle
        right = min(rec1[2], rec2[2])

        # find largest y from smallest y position of each rectangle
        bottom = max(rec1[1], rec2[1])

        # find smallest y from largest y position of each rectangle
        top = min(rec1[3], rec2[3])

        return left < right and bottom < top
