using namespace std;

#include <iostream>
#include <vector>

class AllMissingNumbers {
public:
    static vector<int> findNumbers(vector<int> &nums) {
        // sort the numbers
        int i = 0;
        while (i < nums.size()) {
            // -1 because the numbers are between 1-9
            int correctIndex = nums[i] - 1;

            if (nums[i] != nums[correctIndex]) {
                swap(nums, i, correctIndex);
            } else {
                i++;
            }
        }

        vector<int> missingNumbers;
        for (i = 0; i < nums.size(); i++) {
            // +1 because nums are between 1-9, so index 0 has number 1.
            if (nums[i] != i + 1) {
                missingNumbers.push_back(i + 1);
            }
        }

        return missingNumbers;
    }
    
private:
    static void swap(vector<int> &arr, int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
};

int main(int argc, char *argv[]) {
    vector<int> arr = {2, 3, 1, 8, 2, 3, 5, 1};
    vector<int> missing = AllMissingNumbers::findNumbers(arr);
    cout << "Missing numbers: ";
    for (auto num : missing) {
        cout << num << " ";
    }
    cout << endl;

    arr = {2, 4, 1, 2};
    missing = AllMissingNumber::findNumbers(arr);
    cout << "Missing numbers: ";
    for (auto num : missing) {
        cout << num << " ";
    }
    cout << endl;

    arr = {2, 3, 2, 1};
    missing = AllMissingNumber::findNumbers(arr);
    cout << "Missing numbers: ";
    for (auto num : missing) {
        cout << num << " ";
    }
    cout << endl;
}
