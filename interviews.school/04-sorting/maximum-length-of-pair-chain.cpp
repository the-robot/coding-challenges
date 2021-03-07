// https://leetcode.com/problems/maximum-length-of-pair-chain/

#include <algorithm>
#include <bits/stdc++.h>
#include <vector>

using namespace std;

class Solution {
public:
    int findLongestChain(vector<vector<int>>& pairs) {
        sort(pairs.begin(), pairs.end(), [](const vector<int>& a, const vector<int>& b) -> bool {
            return a[1] < b[1];
        });

        int cur = INT_MIN;
        int ans = 0;

        for (auto pair : pairs) {
            if (cur < pair[0]) {
                cur = pair[1];
                ans++;
            }
        }

        return ans;
    }
};
