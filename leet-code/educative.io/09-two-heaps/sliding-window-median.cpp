// https://leetcode.com/problems/sliding-window-median/

using namespace std;

#include <queue>
#include <unordered_map>
#include <vector>

class Solution {
public:
    vector<double> medianSlidingWindow(vector<int>& nums, int k) {
        vector<double> median;
        unordered_map<int, int> oldNumHash; // map to hold old window nums which are still in lowPq/highPq
        priority_queue<int> lowPq; // maxHeap, PQ to hold lower half of window
        priority_queue<int, vector<int>, greater<int> > highPq; // minHeap, PQ to hold upper half of window

        // add up to k numbers
        for (int i = 0; i < k; ++i) {
            lowPq.push(nums[i]);
        }
        // adjust 2 priority queues
        for (int i = k/2; i > 0; --i) {
            highPq.push(lowPq.top()), lowPq.pop();
        }

        for (int i = k; ; ++i) {
            // calculate medium
            if (k % 2) {
                median.push_back(lowPq.top());
            } else {
                median.push_back(((double)lowPq.top() + highPq.top()) / 2);
            }

            // traversed all numbers
            if (i == nums.size()) {
                break;
            }

            // remove left-most number
            int balance = 0;
            int oldNum = nums[i-k], newNum = nums[i];
            if (oldNum <= lowPq.top()) {
                --balance;
                if (oldNum == lowPq.top()) {
                    lowPq.pop();
                } else {
                    oldNumHash[oldNum]++;
                }
            } else {
                ++balance;
                if (oldNum == highPq.top()) {
                    highPq.pop();
                } else {
                    oldNumHash[oldNum]++;
                }
            }

            // add new number to low/hi priority queue
            if (newNum <= lowPq.top()) {
                ++balance;
                lowPq.push(newNum);
            } else {
                --balance;
                highPq.push(newNum);
            }

            // adjust low/hi priority queue
            if (balance < 0) {
                lowPq.push(highPq.top());
                highPq.pop();
            } else if(balance > 0) {
                highPq.push(lowPq.top());
                lowPq.pop();
            }

            // remove old window numbers
            while(!lowPq.empty() && oldNumHash[lowPq.top()]) {
                oldNumHash[lowPq.top()]--;
                lowPq.pop();
            }
            while(!highPq.empty() && oldNumHash[highPq.top()]) {
                oldNumHash[highPq.top()]--;
                highPq.pop();
            }
        }
        
        return median;
    }
};
