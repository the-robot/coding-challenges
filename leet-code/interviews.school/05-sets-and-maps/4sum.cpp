// https://leetcode.com/problems/4sum/

#include <algorithm>
#include <vector>

using namespace std;

// this solution is very similar to 3sum solution.
class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        vector<vector<int>> result;
        sort(nums.begin(), nums.end());

        for (int i = 0; i < nums.size(); i++) {
            int target_3 = target - nums[i];

            for (int j = i + 1; j < nums.size(); j++) {
                int target_2 = target_3 - nums[j];

                int left = j + 1;
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
                        result.push_back({nums[i], nums[j], added_left, added_right});
                        
                        // Processing the duplicates of number 3
                        while (left < right && nums[left] == added_left) ++left;
                    
                        // Processing the duplicates of number 4
                        while (left < right && nums[right] == added_right) --right;
                    }
                }
                
                // Processing the duplicate of j
                while (j + 1 < nums.size() && nums[j+1] == nums[j]) {
                    j++;
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
