// https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

using namespace std;

#include <vector>

class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        int i = 0;
        while (i < nums.size()) {
            // nums[i] - 1 because numbers are between 1-9
            if (nums[i] > 0 && nums[i] <= nums.size() && nums[i] != nums[nums[i] - 1]) {
                swap(nums[i], nums[nums[i] - 1]);
            } else {
                i++;
            }
        }

        vector<int> missingNumbers;
        for (i = 0; i < nums.size(); i++) {
            if (nums[i] != i + 1) {
                missingNumbers.push_back(i + 1);
            }
        }

        return missingNumbers;
    }
};