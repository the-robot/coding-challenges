using namespace std;

#include <iostream>
#include <string>
#include <vector>

class FindCorruptPair {
public:
    static vector<int> findNumbers(vector<int> &nums) {
        int i = 0;
        while (i < nums.size()) {
            int correctIndex = nums[i] - 1; // -1 because nums are between 1-9

            if (nums[i] != nums[correctIndex]) {
                swap(nums, i, correctIndex);
            } else {
                i++;
            }
        }

        for (i = 0; i < nums.size(); i++) {
            if (nums[i] != i + 1) {
                return vector<int>{nums[i], i + 1};
            }
        }

        return vector<int>{-1, -1};
    }

private:
    static void swap(vector<int> &nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
};

int main() {
    vector<int> arr = {3, 1, 2, 5, 2};
    vector<int> nums = FindCorruptPair::findNumbers(arr);
    cout << nums[0] << ", " << nums[1] << endl;

    arr = {3, 1, 2, 3, 6, 4};
    nums = FindCorruptPair::findNumbers(arr);
    cout << nums[0] << ", " << nums[1] << endl;
}
