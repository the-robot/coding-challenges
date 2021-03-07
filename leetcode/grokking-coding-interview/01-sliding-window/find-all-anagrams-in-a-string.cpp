// https://leetcode.com/problems/find-all-anagrams-in-a-string/

#include <string>
#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
    public:
        vector<int> findAnagrams(string s, string p) {
            // hashmap to calculate frequencies of all the characters in the pattern
            unordered_map<char, int> patternFreq;
            for (auto c : p) {
                patternFreq[c]++;
            }

            vector<int> resultIndices;
            int left = 0, matched = 0;

            for (int right = 0; right < s.length(); right++) {
                char rightChar = s[right];

                if (patternFreq.find(rightChar) != patternFreq.end()) {
                    // decrement the frequency of the matched character
                    patternFreq[rightChar]--;
                    // character is completely matched if freq becomes 0
                    if (patternFreq[rightChar] == 0) {
                        matched++;
                    }
                }
                
                if (matched == (int)patternFreq.size()) {
                    resultIndices.push_back(left);
                }
                
                // shrink the window
                if (right >= p.length() - 1) {
                    char leftChar = s[left++];

                    // if the character going out was part of the pattern, put it back in the frequency
                    if (patternFreq.find(leftChar) != patternFreq.end()) {
                        if (patternFreq[leftChar] == 0) {
                            matched--;
                        }
                        // put the character back for matching
                        patternFreq[leftChar]++;
                    }
                }
            }
            
            return resultIndices;
        }
};
