// https://www.educative.io/courses/grokking-the-coding-interview/JPKr0kqLGNP

#include <vector>

using namespace std;

class MaxSumSubArrayOfSizeK {
    public:
        static int findMaxSumSubArray(int k, const vector<int>& arr) {
            int windowSum = 0, maxSum = 0;
            int left = 0;

            for (int right = 0; right < arr.size(); right++) {
                windowSum += arr[right];  // add the next element
                // slide the window, we don't need to slide if we've not hit the required window size of 'k'
                if (right >= k - 1) {
                    maxSum = max(maxSum, windowSum);
                    windowSum -= arr[left];  // subtract the element going out
                    left++;                  // slide the window ahead
                }
            }

            return maxSum;
        }
};
