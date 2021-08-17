# https://leetcode.com/problems/meeting-rooms-ii/

from heapq import heappush, heappop

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # sort the intervals
        intervals.sort()
        
        rooms = 0
        
        min_heap = [] # to store on-going meeting
        
        for meeting in intervals:
            # remove all meetings that have ended
            while min_heap and self.after(meeting, min_heap[0]):
                heappop(min_heap)
            
            # add the current meeting to min_heap
            start = meeting[0]
            end = meeting[1]
            
            # we put end in front, because we want to sort by meeting end time.
            heappush(min_heap, (end, start))
            
            # all meetings that are on-going, we will need room for each of them
            rooms = max(rooms, len(min_heap))
        
        return rooms

    def after(self, new_meeting: List[int], previous_meeting: List[int]) -> bool:
        """
        Actually every meeting format should be [start, end]
        
        But for those in min_heap, I swapped to [end, start] because I want min_heap
        to pop by finished ones (which is end time).
        
        When I want to check if next meeting overlaps with previous, I have to check
        start time of current (index 0) with end time of previous (index 0 because I swapped).
        """
        
        return new_meeting[0] >= previous_meeting[0]
