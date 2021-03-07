// https://leetcode.com/problems/find-all-duplicates-in-an-array/

using namespace std;

#include <vector>

class Solution {
public:
    vector<int> findDuplicates(vector<int>& nums) {
        int i = 0;
        while (i < nums.size()) {
            // number are between 1-9, so - 1
            int correctIndex = nums[i] - 1;

            if (nums[i] != nums[correctIndex]) {
                swap(nums, i, correctIndex);
            } else {
                i++;
            }
        }

        vector<int> duplicateNumbers;
        for (i = 0; i < nums.size(); i++) {
            if (nums[i] != i + 1) {
                duplicateNumbers.push_back(nums[i]);
            }
        }

        return duplicateNumbers;
    }

private:
    static void swap(vector<int> &arr, int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
};