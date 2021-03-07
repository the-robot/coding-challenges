// https://leetcode.com/problems/3sum/

#include <algorithm>
#include <vector>
#include <unordered_set>

using namespace std;

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> result;
        sort(nums.begin(), nums.end());

        for (int i = 0; i < nums.size(); i++) {
            int target_2 = 0 - nums[i];
            int left = i + 1;
            int right = nums.size() - 1;
            
            while (left < right) {
                int two_sum = nums[left] + nums[right];

                // if sum is still less than target; increment left
                if (two_sum < target_2) {
                    left++;    
                }
                // if sum is greater than target; decrement right
                else if (two_sum > target_2) {
                    right--;
                }
                // else means they are valid numbers
                else {
                    int added_left = nums[left];
                    int added_right = nums[right];
                    result.push_back({nums[i], added_left, added_right});

                    // Processing the duplicates of number 3
                    while (left < right && nums[left] == added_left) ++left;

                    // Processing the duplicates of number 4
                    while (left < right && nums[right] == added_right) --right;
                }
            }

            // Processing the duplicate of i
            while (i + 1 < nums.size() && nums[i+1] == nums[i]) {
                i++;
            }
        }
        
        return result;
    }
};
