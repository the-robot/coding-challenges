# https://leetcode.com/problems/task-scheduler/

from typing import List
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        frequencies = {}
        for char in tasks:
            frequencies[char] = frequencies.get(char, 0) + 1
        
        """
        add all tasks to the maxHeap
        we use maxHeap because we want to do tasks that has most frequencies
        first, so that we can put some other task in between to prevent same
        task running N nearer.
        """
        maxHeap = []
        for char, freq in frequencies.items():
            heapq.heappush(maxHeap, [-freq, char])
            
        intervalCount = 0
        while maxHeap:
            waitList = []
            
            # try to execute as many as 'n+1' tasks from the maxHeap
            k = n + 1
            
            while maxHeap and k > 0:
                intervalCount += 1
                
                freq, char = heapq.heappop(maxHeap)
                if -freq > 1:
                    # decrement the frequency and add to the waitList
                    # + 1 because freq is negative from maxHeap
                    waitList.append((freq + 1, char))
                
                k -= 1
        
            # put all the waiting list back on the heap
            for freq, char in waitList:
                # freq is already negative as it is popped from maxHeap before
                # so no need to * -1
                heapq.heappush(maxHeap, [freq, char])
        
            if maxHeap:
                # we'll be having 'n' idel intervals for the next iteration
                intervalCount += k
        
        return intervalCount
