using namespace std;

#include <iostream>
#include <unordered_set>
#include <vector>

class FirstKMissingPositive {
public:
    static vector<int> findNumbers(vector<int> &nums, int k) {
        int i = 0;
        while (i < nums.size()) {
            if (nums[i] > 0 && nums[i] <= nums.size() && nums[i] != nums[nums[i] - 1]) {
                swap(nums, i, nums[i] - 1);
            } else {
                i++;
            }
        }

        vector<int> missingNumbers;
        unordered_set<int> extraNumbers;
        for (i = 0; i < nums.size() && missingNumbers.size() < k; i++) {
            if (nums[i] != i + 1) {
                missingNumbers.push_back(i + 1);
                extraNumbers.insert(nums[i]);
            }
        }

        // add the remaining missing numbers
        for (i = 1; missingNumbers.size() < k; i++) {
            int candidateNumber = i + nums.size();
            // ignore if the array contains the candidate number
            if (extraNumbers.find(candidateNumber) == extraNumbers.end()) {
                missingNumbers.push_back(candidateNumber);
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

int main() {
    vector<int> arr = {3, -1, 4, 5, 5};
    vector<int> missingNumbers = FirstKMissingPositive::findNumbers(arr, 3);
    cout << "Missing numbers: ";
    for (int num : missingNumbers) {
        cout << num << " ";
    }
    cout << endl;

    arr = {2, 3, 4};
    missingNumbers = FirstKMissingPositive::findNumbers(arr, 3);
    cout << "Missing numbers: ";
    for (int num : missingNumbers) {
        cout << num << " ";
    }
    cout << endl;

    arr = {-2, -3, 4};
    missingNumbers = FirstKMissingPositive::findNumbers(arr, 2);
    cout << "Missing numbers: ";
    for (int num : missingNumbers) {
        cout << num << " ";
    }
    cout << endl;
}
