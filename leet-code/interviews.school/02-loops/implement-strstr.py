# https://leetcode.com/problems/implement-strstr/


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # get needle lengths
        hayLength = len(haystack)
        needleLength = len(needle)

        # edge cases
        if needleLength == 0:
            return 0
        if needleLength > hayLength:
            return -1
        
        # find needle in haystack
        for hayIndex in range(hayLength):
            if haystack[hayIndex: hayIndex + needleLength] == needle:
                return hayIndex
        
        # reaching here means needle not found
        return -1


class RainKarpSolution:
    """
    https://leetcode.com/problems/implement-strstr/discuss/694529/Easy-Rabin-Karp-solution-using-python
    """
    def strStr(self, haystack: str, needle: str) -> int:
        lenHaystack, lenNeedle = len(haystack), len(needle)
        if lenNeedle > lenHaystack: # Initial check for validity of pattern
            return -1

        hashString, hashPattern = 0, 0 # instantiate the hash values

        for i in range(lenNeedle): # calculate the needle hash and initial haystack hash
            hashString += ord(haystack[i])
            hashPattern += ord(needle[i])

        start, end = 0, lenNeedle # initialize the pointers
        for index in range(lenHaystack - lenNeedle + 1): # start string matching
            if hashString == hashPattern: # check if the hashvalues match
                if haystack[start:end] == needle: # check if the pattern match
                    return index

            if end <= lenHaystack-1: # check if the "end" pointer is valid
                # calculate the hash for new window
                hashString -= ord(haystack[start]) 
                hashString += ord(haystack[end])
                start += 1
                end += 1

        return -1
