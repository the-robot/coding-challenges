// https://leetcode.com/problems/valid-anagram/

#include <iostream>
#include <algorithm>

class Solution {
public:
    void sortString(std::string &s) {
        std::sort(s.begin(), s.end());
    }

    bool isAnagram(std::string s, std::string t) {
        sortString(s);
        sortString(t);
        return s == t;
    }
};
