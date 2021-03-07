// https://www.educative.io/courses/grokking-the-coding-interview/3jEXWgB5ZmM

using namespace std;

#include <iostream>
#include <vector>

class FirstMissingPositive {
public:
    static int findNumber(vector<int> &nums) {
        int i = 0;
        while (i < nums.size()) {
            // correctIndex is -1 because, not all test cases have 0
            int correctIndex = nums[i] - 1;
            if (nums[i] > 0 && nums[i] <= nums.size() && nums[i] != nums[correctIndex]) {
                swap(nums, i, correctIndex);
            } else {
                i++;
            }
        }

        for (i = 0; i < nums.size(); i++) {
            if (nums[i] != i + 1) {
                return i + 1;
            }
        }

        return nums.size() + 1;
    }

private:
    static void swap(vector<int> &nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
};

int main() {
    vector<int> nums = {-3, 1, 5, 4, 2};
    cout << FirstMissingPositive::findNumber(nums) << endl;

    nums = {3, -2, 0, 1, 2};
    cout << FirstMissingPositive::findNumber(nums) << endl;

    nums = {3, 2, 5, 1};
    cout << FirstMissingPositive::findNumber(nums) << endl;
}
