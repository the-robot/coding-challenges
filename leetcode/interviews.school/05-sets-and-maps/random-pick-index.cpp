// https://leetcode.com/problems/random-pick-index/

#include <cstdlib>
#include <vector>
#include <unordered_map>

using namespace std;

class Solution {

private:
    unordered_map<int, vector<int>> indices;

public:
    Solution(vector<int>& nums) {
        for (int i = 0; i < nums.size(); i++) {
            this->indices[nums[i]].push_back(i);
        }
    }
    
    int pick(int target) {
        int l = indices[target].size();
        // pick an index at random
        return indices[target][rand() % l];
    }
};
