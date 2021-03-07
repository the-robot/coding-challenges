// https://www.lintcode.com/problem/employee-free-time/
#include <algorithm>
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
    /**
     * @param schedule: a list schedule of employees
     * @return: Return a list of finite intervals 
     */
    vector<Interval> employeeFreeTime(vector<vector<int>> &schedule) {
        vector<Interval> result;
        if (schedule.empty()) {
            return result;
        }
        
        // priority queue to store one interval from each employee
        priority_queue<pair<Interval, pair<int, int>>, vector<pair<Interval, pair<int, int>>>, startCompare> minHeap;
        
        // insert the first interval from each employee
        for (int i = 0; i < schedule.size(); i++) {
            minHeap.push(make_pair(schedule[i][0], make_pair(i, 0)));
        }
        
        Interval previousInterval = minHeap.top().first;
        
        while (!minHeap.empty()) {
            auto queueTop = minHeap.top();
            minHeap.pop();
            
            // if previousInterval is not overlapping with the next interval, insert a free interval
            if (previousInterval.end < queueTop.first.start) {
                result.push_back({previousInterval.end, queueTop.first.start});
                previousInterval = queueTop.first;
            } else {
                // overlapping intervals, update the previousInterval if needed
                if (previousInterval.end < queueTop.first.end) {
                    previousInterval = queueTop.first;
                }
            }
            
            // if there are more intervals available for the same employee; add their next Interval
            vector<Interval> employeeSchedule = schedule[queueTop.second.first];
            if (employeeSchedule.size() > queueTop.second.second + 1) {
                minHeap.push( make_pair(
                        employeeSchedule[queueTop.second.second+1],
                        make_pair(queueTop.second.first, queueTop.second.second + 1)));
            }
        }
        
        return result;
    }

private:
    struct startCompare {
        bool operator()(const pair<Interval, pair<int, int>> &x, const pair<Interval, pair<int, int>> &y) {
            return x.first.start > y.first.start;
        }
    };
};
