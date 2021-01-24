// https://leetcode.com/problems/4sum-ii/

#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
public:
    int fourSumCount(vector<int>& A, vector<int>& B, vector<int>& C, vector<int>& D) {
        if (A.size() == 0) {
            return 0;
        }
        
        unordered_map<int, int> m;
        int count = 0;
        
        for (auto i : C) {
            for (auto j : D) {
                m[i+j]++;
            }
        }
        
        for (auto i : A) {
            for (auto j : B) {
                int x = -1 * (i+j);
                count += m[x];
            }
        }
        
        return count;
    }
};
