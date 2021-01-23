// https://leetcode.com/problems/subarray-sum-equals-k/

#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        // first int is sum and second int is number of times
        // we have seen that sum
        unordered_map<int, int> arr_sums;
        arr_sums[0] = 1;
        
        int sum = 0;
        int result = 0;
        
        for (int i = 0; i < nums.size(); i++) {
            sum += nums[i];
            
            if (arr_sums.find(sum-k) != arr_sums.end()) {
                result += arr_sums[sum-k];
            }
            
            if (arr_sums.find(sum) == arr_sums.end()) {
                arr_sums[sum] = 1;
            } else {
                arr_sums[sum]++;
            }
        }
        
        return result;
    }
};
