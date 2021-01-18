// https://leetcode.com/problems/group-anagrams/

#include <algorithm>
#include <map>
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> result;
        map<string, vector<string>> anagrams;

        for (string str : strs) {
            // sort the string to find as key
            string sorted = str;
            sort(sorted.begin(), sorted.end());

            // find pos in the map
            auto pos = anagrams.find(sorted);

            // create new bucket if not exists
            if (pos == anagrams.end()) {
                vector<string> bucket = {str};
                anagrams[sorted] = bucket;
                continue;
            }

            // add to existing bucket
           pos->second.push_back(str);
        }

        // add the groups back to result
        for (auto it = anagrams.begin(); it != anagrams.end(); it++) {
            result.push_back(it->second);
        }

        return result;
    }
};
