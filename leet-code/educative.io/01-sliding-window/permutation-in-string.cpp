// https://leetcode.com/problems/permutation-in-string/

#include <string>
#include <unordered_map>

using namespace std;

class Solution {
    public:
        bool checkInclusion(string s1, string s2) {
            // hashmap to calculate frequencies of all the characters in the pattern
            unordered_map<char, int> patternFreq;
            for (auto c : s1) {
                patternFreq[c]++;
            }
            
            int left = 0, matched = 0;
            
            for (int right = 0; right < s2.length(); right++) {
                char rightChar = s2[right];
                
                if (patternFreq.find(rightChar) != patternFreq.end()) {
                    // drecrement the frequency of the matched character
                    patternFreq[rightChar]--;
                    // character is completely matched if freq becomes 0
                    if (patternFreq[rightChar] == 0) {
                        matched++;
                    }
                }
                
                if (matched == (int)patternFreq.size()) {
                    return true;
                }
                
                // shrink the window
                if (right >= s1.length() - 1) {
                    char leftChar = s2[left++];
                    
                    // if the character going out was part of the pattern, put it back in the frequency
                    if (patternFreq.find(leftChar) != patternFreq.end()) {
                        if (patternFreq[leftChar] == 0) {
                            matched--;  // before putting the character back, decrement the matched count
                        }
                        // put the character back for matching
                        patternFreq[leftChar]++;
                    } 
                }
            }
            
            return false;
        }
};
