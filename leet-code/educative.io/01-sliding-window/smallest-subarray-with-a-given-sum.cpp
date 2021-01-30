// https://www.educative.io/courses/grokking-the-coding-interview/7XMlMEQPnnQ

#include <limits>
#include <vector>

using namespace std;

class MinSizeSubArraySum {
    public:
        static int findMinSubArray(int S, const vector<int>& arr) {
            int minLength = numeric_limits<int>::max();
            int sum = 0;
            int left = 0;

            for (int right = 0; right < arr.size(); right++) {
                sum += arr[right];

                while (sum >= S) {
                    minLength = min(minLength, right - left + 1);
                    sum -= arr[left];
                    left++;
                }
            }

            return minLength == numeric_limits<int>::max() ? 0 : minLength;
        }
};
