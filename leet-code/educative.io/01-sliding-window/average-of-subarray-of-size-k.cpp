// https://www.educative.io/courses/grokking-the-coding-interview/JPKr0kqLGNP

#include <vector>

using namespace std;

class MaxSumSubArrayOfSizeK {
    public:
        static int findMaxSumSubArray(int k, const vector<int>& arr) {
            int maxSum = 0;
            int sum = 0;
            int left = 0;

            for (int right = 0; right < arr.size(); right++) {
                sum += arr[right];

                if (right >= k - 1) {
                    maxSum = max(maxSum, sum);
                    sum -= arr[left];
                    left++;
                }
            }

            return maxSum;
        }
};
