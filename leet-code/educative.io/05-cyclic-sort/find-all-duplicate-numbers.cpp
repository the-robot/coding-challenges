using namespace std;

#include <iostream>
#include <vector>

class FindAllDuplicate {
    public:
    static vector<int> findNumbers(vector<int> &nums) {
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

int main() {
    vector<int> arr = {3, 4, 4, 5, 5};
    vector<int> duplicates = FindAllDuplicate::findNumbers(arr);
    cout << "Duplicates are: ";
    for (auto num : duplicates) {
        cout << num << " ";
    }
    cout << endl;

    arr = {5, 4, 7, 2, 3, 5, 3};
    duplicates = FindAllDuplicate::findNumbers(arr);
    cout << "Duplicates are: ";
    for (auto num : duplicates) {
        cout << num << " ";
    }
    cout << endl;
}
