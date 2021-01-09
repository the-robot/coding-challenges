// https://leetcode.com/problems/two-sum/submissions/

#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> um;
        
        for (int i=0; i<nums.size(); i++) {
            int number = nums[i];
            int pair = target - number;
            
            if (um.find(pair) != um.end()) {
                return vector<int>{um[pair], i};
            }

            um[number] = i;
        }

        return vector<int>{};
    }
};
