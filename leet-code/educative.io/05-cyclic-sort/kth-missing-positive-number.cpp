// https://leetcode.com/problems/kth-missing-positive-number/

using namespace std;

#include <unordered_set>
#include <vector>

class Solution {
public:
    int findKthPositive(vector<int>& arr, int k) {
        int i = 0;
        while (i < arr.size()) {
            if (arr[i] > 0 && arr[i] <= arr.size() && arr[i] != arr[arr[i] - 1]) {
                swap(arr[i], arr[arr[i] - 1]);
            } else {
                i++;
            }
        }
        
        vector<int> missingNumbers;
        unordered_set<int> extraNumbers;
        for (i = 0; i < arr.size() && missingNumbers.size() < k; i++) {
            if (arr[i] != i + 1) {
                missingNumbers.push_back(i + 1);
                extraNumbers.insert(arr[i]);
            }
        }
        
        // add the remaining missing numbers
        for (i = 1; missingNumbers.size() < k; i++) {
            int candidateNumber = i + arr.size();
            // ignore if the array contains the candidate number
            if (extraNumbers.find(candidateNumber) == extraNumbers.end()) {
                missingNumbers.push_back(candidateNumber);
            }
        }
        
        return missingNumbers[k-1];
    }
};