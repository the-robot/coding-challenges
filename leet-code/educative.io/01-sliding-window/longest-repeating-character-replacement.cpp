// https://leetcode.com/problems/longest-repeating-character-replacement/

#include <string>
#include <unordered_map>

using namespace std;

class Solution {
    public:
        int characterReplacement(string s, int k) {
            unordered_map<char, int> seen;
            int maxLength = 0;
            int maxRepeatLetterCount = 0;
            int left = 0;

            for (int right = 0; right < s.size(); right++) {
                char rightChar = s[right];
                seen[rightChar]++;
                maxRepeatLetterCount = max(maxRepeatLetterCount, seen[rightChar]);

                if (right - left + 1 - maxRepeatLetterCount > k) {
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
