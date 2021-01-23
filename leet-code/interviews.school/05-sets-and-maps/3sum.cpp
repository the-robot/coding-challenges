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
        vector<vector<int>> output;
        sort(nums.begin(), nums.end());

        for (int i = 0; i < nums.size(); i++) {
            // skip duplicate;
            if (i != 0 && nums[i] == nums[i-1]) {
                continue;
            }
            
            int j = i + 1;
            int k = nums.size() - 1;
            while (j < k) {
                if (nums[i] + nums[j] + nums[k] == 0) {
                    output.push_back({nums[i], nums[j], nums[k]});
                    j++;
                    
                    // skip duplicate
                    while (j < k && nums[j] == nums[j-1]) {
                        j++;
                    }
                } else if (nums[i] + nums[j] + nums[k] < 0) {
                    // because we are sorted; we knows that k holds number
                    // larger than j. if combination is less than 0
                    // we increment j instead of decrementing k
                    // so that the combination will become > 0
                    j++;
                } else {
                    k--;
                }
            }
        }
        
        return output;
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
