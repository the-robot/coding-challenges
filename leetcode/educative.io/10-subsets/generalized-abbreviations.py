# https://www.lintcode.com/problem/generalized-abbreviation/

from collections import deque
from typing import List

class AbbreviatedWord:
    def __init__(self, listString: List[str], index: int, count: int):
        self.str = listString
        # the current word index
        self.index = index
        # total abbreviation (as underscore in whiteboard) count
        # at the current index, (counts after alphabet)
        # i.e. 1A_ has count 0
        #      ___ has count 3
        self.count = count

class Solution:
    """
    @param word: the given word
    @return: the generalized abbreviations of a word
    """
    def generateAbbreviations(self, word):
        wordLen = len(word)
        result = []
        queue = deque()
        queue.append( AbbreviatedWord(list(), 0, 0) )

        while queue:
            abWord = queue.popleft()

            if abWord.index == wordLen: # reaches the end
                if abWord.count != 0:
                    abWord.str.append(str(abWord.count))
                result.append(''.join(abWord.str))
            else:
                # continue abbreviation by incrementing the current abbreviation count
                queue.append(
                    AbbreviatedWord(list(abWord.str), abWord.index + 1, abWord.count + 1)
                )

                # restart abbreviation, append the count and the current character to the string
                if abWord.count != 0:
                    abWord.str.append(str(abWord.count))
                
                newWord = list(abWord.str)
                newWord.append(word[abWord.index])
                queue.append(
                    AbbreviatedWord(newWord, abWord.index + 1, 0)
                )

        return result
