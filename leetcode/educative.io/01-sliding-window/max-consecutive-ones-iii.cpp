// https://leetcode.com/problems/max-consecutive-ones-iii/

#include <vector>

using namespace std;

class Solution {
public:
    int longestOnes(vector<int>& A, int K) {
        int maxLength = 0;
        int maxOnesCount = 0;
        int left = 0;
        
        for (int right = 0; right < A.size(); right++) {
            if (A[right] == 1) {
                maxOnesCount++;
            }
            
            if (right - left + 1 - maxOnesCount > K) {
                if (A[left] == 1) {
                    maxOnesCount--;
                }
                left++;
            }
            
            maxLength = max(maxLength, right - left + 1);
        }
        
        return maxLength;
    }
};
