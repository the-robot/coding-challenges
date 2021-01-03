// https://leetcode.com/problems/merge-intervals/

#include <algorithm>
#include <iostream>
#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> merge(std::vector<std::vector<int>>& intervals) {
        std::vector<std::vector<int>> result;
        
        // sort the numbers
        sort(intervals.begin(), intervals.end());
        std::vector<std::vector<int>>::const_iterator it = intervals.cbegin();

        while (it != intervals.cend()) {
            std::vector<int> merged = *it++;

            while (it != intervals.cend() && merged[1] >= (*it)[0]) {
                merged[1] = std::max(merged[1], (*it)[1]);
                it++;
            }

            result.push_back(merged);
        }

        return result;
    }
};
