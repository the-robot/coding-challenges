// https://leetcode.com/problems/missing-number/

using namespace std;

#include <vector>

class Solution {
public:
    int missingNumber(vector<int>& nums) {
        // sort the numbers
        int i = 0;
        while (i < nums.size()) {
            int correctIndex = nums[i];
            
            if (nums[i] < nums.size() && nums[i] != nums[correctIndex]) {
                swap(nums, i, correctIndex);
            } else {
                i++;
            }
        }

        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] != i) {
                return i;
            }
        }
        
        return nums.size();
    }

private:
    static void swap(vector<int> &arr, int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
};
