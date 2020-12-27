// https://leetcode.com/problems/contains-duplicate

#include <algorithm>
#include <vector>

class Solution {
public:
    bool containsDuplicate(std::vector<int>& nums) {
        // edge case; empty vector
        if (nums.size() == 0) {
            return false;
        }

        std::sort(nums.begin(), nums.end());

        for (int i=0; i<nums.size()-1; i++) {
            if (nums[i] == nums[i+1]) {
                return true;
            }
        }

        return false;
    }
};
