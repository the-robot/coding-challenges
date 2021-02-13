using namespace std;

#include <iostream>
#include <vector>

class MissingNumber {
public:
    static int findMissingNumber(vector<int> &nums) {
        // sort the number
        int i = 0;
        while (i < nums.size()) {
            // supposed to be correct index; 1 for i = 1
            int correctIndex = nums[i];

            // if correct index is not equal to the value getting by nums[correctIndex]
            if (nums[i] != nums[correctIndex]) {
                swap(nums, i, correctIndex);
            } else {
                i++;
            }
        }

        // find missing number by it's index
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

int main(int argc, char *argv[]) {
    vector<int> arr = {4, 0, 3, 1};
    int number = MissingNumber::findMissingNumber(arr);
    cout << "Missing number: " << number << endl;

    arr = vector<int>{8, 3, 5, 2, 4, 6, 0, 1};
    number = MissingNumber::findMissingNumber(arr);
    cout << "Missing number: " << number << endl;
}
