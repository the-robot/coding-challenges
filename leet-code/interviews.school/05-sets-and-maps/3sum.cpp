// https://leetcode.com/problems/3sum/

#include <algorithm>
#include <map>
#include <vector>
#include <unordered_set>

using namespace std;

// this is the best solution without using extra memory like hashmap solution.
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

// O(n^2) faster than the dumbest solution but
// will fail because heap overflow from unordered_set.
class HashMapSolution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> output;
        sort(nums.begin(), nums.end());

        for (int i = 0; i < nums.size(); i++) {
            if (i != 0 && nums[i] == nums[i-1]) {
                continue;
            }
            unordered_set<int> seen;

            for (int j = i + 1; j < nums.size(); j++) {
                int pair = -nums[i] - nums[j];
                if (seen.find(pair) != seen.end()) {
                    output.push_back({nums[i], nums[j], pair});
                    
                    // skip duplicate;
                    while (j != i + 1 && nums[j] == nums[j-1]) {
                        j++;
                    }
                }

                seen.insert(nums[j]);
            }

        }
        
        return output;
    }
};

// slow AF, its O(n^3).
class NaiveSolution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> output;
        sort(nums.begin(), nums.end());

        for (int i = 0; i < nums.size(); i++) {
            if (i != 0 && nums[i] == nums[i-1]) {
                continue;
            }

            for (int j = i + 1; j < nums.size(); j++) {
                if (j != i + 1 && nums[j] == nums[j-1]) {
                    continue;
                }

                for (int k = j + 1; k < nums.size(); k++) {
                    if (k != j + 1 && nums[k] == nums[k-1]) {
                        continue;
                    }

                    if (nums[i] + nums[j] + nums[k] == 0) {
                        output.push_back({nums[i], nums[j], nums[k]});
                    }
                }

            }

        }
        
        return output;
    }
};
