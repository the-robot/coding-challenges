// https://leetcode.com/problems/longest-substring-without-repeating-characters/

#include <string>
#include <unordered_map>

using namespace std;

class Solution {
    public:
        int lengthOfLongestSubstring(string s) {
            unordered_map<char, int> seen; 
            int maxLength = 0;
            int left = 0;
            
            for (int right = 0; right < s.size(); right++) {
                char rightChar = s[right];
                seen[rightChar]++;
                
                while (seen[rightChar] > 1) {
                    char leftChar = s[left];
                    seen[leftChar]--;
                    
                    if (seen[leftChar] == 0) {
                        seen.erase(leftChar);
                    }
                    left++;
                }
                
                maxLength = max(maxLength, right - left + 1);
            }
            
            return maxLength;
        }
};
