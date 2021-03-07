# https://leetcode.com/problems/maximum-frequency-stack/

import heapq


class Element:
    def __init__(self, number: int, frequency: int, sequenceNumber: int):
        # value of the number
        self.number = number
        
        # current frequency of the number when it was pushed to the top
        self.frequency = frequency
        
        # to know what number came first
        self.sequenceNumber = sequenceNumber
    
    def __lt__(self, other: 'Element') -> bool:
        """
        So when compare in heapq, maxHeap
        1. higher frequency will be on top (pop first)
        2. if frequency is the same, the element with higher sequenceNumber will be on top (pop first)
           because if tie, we want to pop the number that is added later
        """

        # higher frequency wins
        if self.frequency != other.frequency:
            return self.frequency > other.frequency
    
        # if both element have same frequency, return the element that was pushed later
        return self.sequenceNumber > other.sequenceNumber
        

class FreqStack:
    """Max Heap"""

    def __init__(self):
        self.sequenceNumber = 0
        self.maxHeap = []
        self.frequencyMap = {}

    def push(self, val: int) -> None:
        self.frequencyMap[val] = self.frequencyMap.get(val, 0) + 1
        
        heapq.heappush(self.maxHeap, Element(
            val, self.frequencyMap[val], self.sequenceNumber,
        ))
        
        # increment sequence number
        self.sequenceNumber += 1

    def pop(self) -> int:
        val = heapq.heappop(self.maxHeap).number
        
        # decrement the frequency or remove if this is the last number
        if self.frequencyMap[val] > 1:
            self.frequencyMap[val] -= 1
        else:
            del self.frequencyMap[val]
        
        return val
