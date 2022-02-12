// https://leetcode.com/problems/maximum-product-of-three-numbers/

#include <algorithm>
#include <vector>

class Solution {
public:
    int maximumProduct(std::vector<int>& nums) {
        std::sort(nums.begin(), nums.end());
        int length = nums.size();

        return std::max(
            nums[length-1] * nums[length-2] * nums[length-3],
            nums[0] * nums[1] * nums[length-1]
        );
    }
};
