// https://leetcode.com/problems/contains-duplicate/

#include <algorithm>
#include <vector>
#include <unordered_set>

using namespace std;

// Set solution
class SetSolution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> st;
        
        for (int number : nums) {
            st.insert(number);
        }
        
        return st.size() != nums.size();
    }
};

// Pointer solution (faster than the previous and no extra space)
class PtrSolution {
public:
    bool containsDuplicate(vector<int>& nums) {
        // edge case
        if (nums.size() == 0) {
            return false;
        }

        sort(nums.begin(), nums.end());
        
        for (int i=0; i<nums.size() - 1; i++) {
            if (nums[i] == nums[i+1]) {
                return true;
            }
        }

        return false;
    }
};
