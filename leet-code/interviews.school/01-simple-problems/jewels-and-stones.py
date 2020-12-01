# https://leetcode.com/problems/jewels-and-stones/

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        counts = 0

        for char in S:
            if char in J:
                counts += 1

        return counts
