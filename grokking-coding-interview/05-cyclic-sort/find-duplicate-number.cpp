// https://leetcode.com/problems/find-the-duplicate-number/

using namespace std;

#include <vector>

class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        int i = 0;
        // NOTE: the sort below does not cater for 0 as number;
        //       that's why nums[i] is supposed to be equal to nums[i] + 1.
        //       I.e. [1, 2, 3], number 1 is index, i = 0.
        while (i < nums.size()) {
            if (nums[i] != i + 1) {  // if not sorted
                int correctIndex = nums[i] - 1;

                // if it is not the same as the number from previous index
                if (nums[i] != nums[correctIndex]) {
                    swap(nums, i, correctIndex);
                } else { // if same as previous; means we found the duplicate
                    return nums[i];
                }
            } else {
                i++;
            }
        }

        return -1;
    }
    
private:
    static void swap(vector<int> &arr, int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
};