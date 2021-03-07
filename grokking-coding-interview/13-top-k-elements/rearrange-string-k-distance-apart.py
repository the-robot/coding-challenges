# https://leetcode.com/problems/rearrange-string-k-distance-apart/

from collections import deque
import heapq


class Solution:
    def reorganizeString(self, S: str, k: int) -> str:
        if k <= 1:
            return S

        frequencies = {}
        for char in S:
            frequencies[char] = frequencies.get(char, 0) + 1
        
        """
        add all characters to maxHeap, we use maxHeap because
        we should first append the most frequent characters to
        the output string
        """
        maxHeap = []
        for char, freq in frequencies.items():
            heapq.heappush(maxHeap, [-freq, char])

        queue = deque()
        resultString = []
        while maxHeap:
            freq, char = heapq.heappop(maxHeap)

            # append the current character to the result string and decrement it's count.
            resultString.append(char)

            # decrement the frequency and append to the queue
            queue.append((freq + 1, char)) # freq is neg from maxHeap

            if len(queue) == k:
                freq, char = queue.popleft()
                if -freq > 0:
                    heapq.heappush(maxHeap, [freq, char])

        # if not the same length, means cannot be reorganized in such a way that
        # no two same characters come next to each other.
        return "".join(resultString) if len(resultString) == len(S) else ""


if __name__ == "__main__":
    s = Solution()

    print(s.reorganizeString("Programming", 3))
    print(s.reorganizeString("mmpp", 2))
    print(s.reorganizeString("aab", 2))
    print(s.reorganizeString("aapa", 3))
