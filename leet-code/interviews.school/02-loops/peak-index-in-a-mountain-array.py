# https://leetcode.com/problems/peak-index-in-a-mountain-array/

from typing import List

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        peakIndex = 0

        for i in range(1, len(arr)):
            if arr[i] <= arr[peakIndex]:
                break
            peakIndex = i

        return peakIndex
