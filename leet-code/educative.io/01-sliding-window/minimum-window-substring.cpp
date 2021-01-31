// https://leetcode.com/problems/minimum-window-substring/

#include <string>
#include <unordered_map>

using namespace std;

class Solution {
public:
    string minWindow(string s, string t) {
        // hashmap to calculate frequencies of all the characters in the pattern
        unordered_map<char, int> patternFreq;
        for (auto c : t) {
            patternFreq[c]++;
        }

        int left = 0, matched = 0, minLength = s.length() + 1, subStrStart = 0;

        for (int right = 0; right < s.length(); right++) {
            char rightChar = s[right];

            if (patternFreq.find(rightChar) != patternFreq.end()) {
                // decrement the frequency of the matched character
                patternFreq[rightChar]--;
                // character is completely matched if freq becomes 0
                if (patternFreq[rightChar] >= 0) {
                    matched++;
                }
            }

            // shink the window if we can, finish as soon as we remove a matched character
            while (matched == t.length()) {
                if (minLength > right - left + 1) {
                    minLength = right - left + 1;
                    subStrStart = left;
                }

                char leftChar = s[left++];
                if (patternFreq.find(leftChar) != patternFreq.end()) {
                    // note that we could have redundant matching characters, therefore we'll decrement the
                    // matched count only when a useful occurrence of a matched character is going out of
                    // the window
                    if (patternFreq[leftChar] == 0) {
                        matched--;
                    }
                    
                    patternFreq[leftChar]++;
                }
            }
        }

        return minLength > s.length() ? "" : s.substr(subStrStart, minLength);
    }
};
