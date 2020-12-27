// https://leetcode.com/problems/transpose-matrix/

#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> transpose(std::vector<std::vector<int>>& A) {
        std::vector<std::vector<int>> res;
        res.resize(A[0].size());
        
        for (int i=0; i<A[0].size(); i++) {
            res[i].resize(A.size());
        }

        for (int i=0; i<A.size(); i++) {
            for (int j=0; j<A[i].size(); j++) {
                res[j][i] = A[i][j];
            }
        }

        return res;
    }
};
