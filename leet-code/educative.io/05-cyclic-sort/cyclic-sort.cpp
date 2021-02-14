// https://www.educative.io/courses/grokking-the-coding-interview/B8qXVqVwDKY

using namespace std;

#include <iostream>
#include <vector>

class CyclicSort {
public:
    static void sort(vector<int> &nums) {
        // sort the numbers
        int i = 0;
        while (i < nums.size()) {
            // -1 because the numbers are between 1-9
            int correctIndex = nums[i] - 1;

            // if the number value is not at the correct index;
            // swap with correct index
            if (nums[i] != nums[correctIndex]) {
                swap(nums, i, correctIndex);
            } else {
                i++;
            }
        }
    }

private:
    static void swap(vector<int> &nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
};

int main(int argc, char *argv[]) {
    vector<int> arr = {3, 1, 5, 4, 2};
    CyclicSort::sort(arr);
    for (auto num : arr) {
        cout << num << " ";
    }
    cout << endl;

    arr = vector<int>{2, 6, 4, 3, 1, 5};
    CyclicSort::sort(arr);
    for (auto num : arr) {
        cout << num << " ";
    }
    cout << endl;

    arr = vector<int>{1, 5, 6, 4, 3, 2};
    CyclicSort::sort(arr);
    for (auto num : arr) {
        cout << num << " ";
    }
    cout << endl;
}
