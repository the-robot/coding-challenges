// https://leetcode.com/problems/largest-number/

#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

bool stringSort(std::string a, std::string b) {
    return a+b > b+a;
}

class Solution {
public:
    std::string largestNumber(std::vector<int>& nums) {
        std::vector<std::string> strings(nums.size());

        for (int i = 0; i < nums.size(); i++) {
            strings[i] = std::to_string(nums[i]);
        }
        
        // sort the string
        std::sort(strings.begin(), strings.end(), stringSort);
        
        // edge case; if first number is 0; just return 0
        if (strings[0] == "0") {
            return "0";
        }
        
        // concat string
        std::string result;
        for (std::string x : strings) {
            result += x;
        }

        return result;
    }
};
