# https://leetcode.com/problems/find-smallest-letter-greater-than-target/

from typing import List

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        n = len(letters)
        
        if target < letters[0] or target > letters[n - 1]:
            return letters[0]

        return self.binarySearch(letters, target, 0, n - 1)

    def binarySearch(self, letters: List[str], target: str, left: int, right: int) -> int:        
        if left > right:
            # the reason of using modulo is that, the letters are circular
            # so imagine, you get left is 11 for letters length of 10, it means
            # the letter you have to return is 1, 11 % 10 = 1
            return letters[left % len(letters)]

        # calculate mid number
        mid = int(left + (right - left) / 2)

        if letters[mid] > target:
            return self.binarySearch(letters, target, left, mid - 1)
        else:
            return self.binarySearch(letters, target, mid + 1, right)
