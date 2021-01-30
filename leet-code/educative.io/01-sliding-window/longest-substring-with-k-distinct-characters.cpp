// https://www.educative.io/courses/grokking-the-coding-interview/YQQwQMWLx80

#include <string>
#include <unordered_map>

using namespace std;

class LongestSubstringKDistinct {
    public:
        static int findLength(const string& str, int k) {
            unordered_map<char, int> seen;
            int maxLength = 0;
            int left = 0;
            
            for (int right = 0; right < str.size(); right++) {
                seen[str[right]]++;

                // shink the sliding window, if we have more than 'k' distinct chars
                while ((int)seen.size() > k) {
                    char leftChar = str[left];
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
