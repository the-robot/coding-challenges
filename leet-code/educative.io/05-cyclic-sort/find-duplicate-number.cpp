using namespace std;

#include <iostream>
#include <vector>

class FindDuplicate{
    public:
    static int findNumber(vector<int> &nums) {
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

int main() {
    vector<int> v1 = {1, 4, 4, 3, 2};
    cout << FindDuplicate::findNumber(v1) << endl;

    v1 = {2, 1, 3, 3, 5, 4};
    cout << FindDuplicate::findNumber(v1) << endl;

    v1 = {2, 4, 1, 4, 4};
    cout << FindDuplicate::findNumber(v1) << endl;
}
