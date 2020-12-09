# https://leetcode.com/problems/longest-common-prefix

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # edge case
        if len(strs) == 0:
            return ""

        # by default first word is the longest prefix
        prefix = strs[0]

        for word in strs[1:]:
            # find the shortest word to treverse
            length = min(len(prefix), len(word))

            # treverse by index until indices at both words are mismatch
            index = 0
            while index < length:
                if prefix[index] != word[index]:
                    break
                index += 1

            # slice prefix up to the treversed index
            prefix = prefix[:index]

        return prefix
