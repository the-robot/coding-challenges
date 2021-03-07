# https://leetcode.com/problems/third-maximum-number/

from typing import List

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        fm = sm = tm = None

        for num in nums:
            if fm is None or num > fm:
                tm = sm
                sm = fm
                fm = num
            elif num == fm:
                continue

            elif sm is None or num > sm:
                tm = sm
                sm = num
            elif num == sm:
                continue

            elif tm is None or num > tm:
                tm = num
        
        return fm if tm is None else tm
