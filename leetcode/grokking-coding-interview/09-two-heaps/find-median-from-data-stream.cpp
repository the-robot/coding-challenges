// https://leetcode.com/problems/find-median-from-data-stream/

using namespace std;

#include <queue>
#include <vector>

class MedianFinder {
public:
    /** initialize your data structure here. */
    priority_queue<int> lowPq; // store all small numbers [1, 2, 3, ...]
    priority_queue<int, vector<int>, greater<int> > highPq; // store all large numbers [10, 9, 8, ...]
    MedianFinder() {}
  
    void addNum(int num) {
        if (lowPq.empty() or lowPq.top() > num) {
            lowPq.push(num);
        } else {, 
            highPq.push(num);
        }
        
        if (lowPq.size() > highPq.size() + 1) {
            highPq.push(lowPq.top());
            lowPq.pop();
        } else if (highPq.size() > lowPq.size() + 1) {
            lowPq.push(highPq.top());
            highPq.pop();
        }
    }
    
    double findMedian() {
        if (lowPq.size() == highPq.size()) {
            if (lowPq.empty()) {
                return 0;
            } else {
                return (lowPq.top() + highPq.top()) / 2.0;
            }
        } else {
            return lowPq.size() > highPq.size() ? lowPq.top() : highPq.top();
        }
    }
};

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder* obj = new MedianFinder();
 * obj->addNum(num);
 * double param_2 = obj->findMedian();
 */
