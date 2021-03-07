// https://leetcode.com/problems/top-k-frequent-elements/

#include <map>
#include <queue>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        map<int, int> counter;
        priority_queue<pair<int, int>> queue;
        vector<int> result;
        
        // count frequencies
        for (auto num : nums) {
            if (counter.find(num) == counter.end()) {
                counter[num] = 1;
            } else {
                counter[num]++;
            }
        }
        
        // push into priority queue
        for (auto pair : counter) {
            queue.push(make_pair(pair.second, pair.first));
        }
        
        // get top k
        for (int i = 0; i < k; i++) {
            result.push_back(queue.top().second);
            queue.pop();
        }
        
        return result;
    }
};