// https://www.lintcode.com/problem/meeting-rooms-ii/

#include <algorithm>
#include <iostream>
#include <queue>
#include <vector>

using namespace std;

class Interval {
    int start, end;
    Interval(int start, int end) {
        this->start = start;
        this->end = end;
    }
};

class Solution {
public:
    struct endCompare {
        bool operator()(const Interval &x, const Interval &y) {
            return x.end > y.end;
        }
    };

    /**
     * @param intervals: an array of meeting time intervals
     * @return: the minimum number of conference rooms required
     */
    int minMeetingRooms(vector<Interval> &intervals) {
        // sort the intervals
        sort(
            intervals.begin(),
            intervals.end(),
            [](const Interval &x, const Interval &y) -> bool {
                return x.start < y.start;
            }
        );

        int minRooms = 0;
        priority_queue<Interval, vector<Interval>, endCompare> minHeap; // FIFO
        
        for (auto meeting : intervals) {
            // remove all meeting that have ended
            while (!minHeap.empty() && meeting.start >= minHeap.top().end) {
                minHeap.pop();
            }
            
            // add the current meeting into the minHeap
            minHeap.push(meeting);
            
            // all active meeting are in the minHeap, so we need rooms for all of them.
            minRooms = max(minRooms, (int)minHeap.size());
        }
        
        return minRooms;
    }
};
