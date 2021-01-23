// https://leetcode.com/problems/contains-duplicate-ii/

#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        unordered_map<int, int> m;
        
        for (int i = 0; i < nums.size(); i++) {
            bool found = m.find(nums[i]) != m.end();
            if (found && abs(m[nums[i]] - i) <= k) {
                return true;
            }
            
            m[nums[i]] = i;
        }
        
        return false;
    }
};
