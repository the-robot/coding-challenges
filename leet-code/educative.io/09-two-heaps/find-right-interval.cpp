// https://leetcode.com/problems/find-right-interval/

using namespace std;

#include <queue>
#include <vector>

class Solution {
public:
    vector<int> findRightInterval(vector<vector<int> >& intervals) {
        vector<int> ans(intervals.size(), -1); // default to -1 for no right interval
        
        // heaps for finding maximum start and end (basically sort the pairs from high-low, maxheap)
        priority_queue<pair<int, int> > maxStartHeap;
        priority_queue<pair<int, int> > maxEndHeap;
        
        for (int i = 0; i < intervals.size(); ++i) {
            maxStartHeap.push( make_pair(intervals[i][0], i) );
            maxEndHeap.push( make_pair(intervals[i][1], i) );
        }

        for (int i = 0; i < intervals.size(); ++i) {
            // find the next interval of the intervals which has the highest 'end'
            pair<int, int> endPair = maxEndHeap.top(); // {value, index}
            maxEndHeap.pop();
            
            int topEnd = endPair.first, endIndex = endPair.second;
            
            
            if (maxStartHeap.top().first >= topEnd) {
                pair<int, int> startPair = maxStartHeap.top(); // {value, index}
                maxStartHeap.pop();
                
                int topStart = startPair.first, startIndex = startPair.second;
                
                // find the interval that has the closest 'start'
                while (!maxStartHeap.empty() && maxStartHeap.top().first >= topEnd) {
                    startPair = maxStartHeap.top();
                    maxStartHeap.pop();
                    
                    topStart = startPair.first, startIndex = startPair.second;
                }
                
                // add index
                ans[endIndex] = startIndex;
                // put the interval back as it could be next interval of other intervals
                maxStartHeap.push(startPair);
            }
            
        }
        
        return ans;
    }
};
