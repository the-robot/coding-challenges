// https://leetcode.com/problems/word-pattern/

#include <string>
#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
public:
    bool wordPattern(string pattern, string s) {
        vector<string> words = split(s);

        unordered_map<char, string> mapChar;
        unordered_map<string, char> mapWord;

        // if pattern chars and string words count is different
        // return false straight away
        if (pattern.size() != words.size()) {
            return false;
        }

        for (int i = 0; i < pattern.size(); i++) {
            char c = pattern[i];
            string w = words[i];

            bool foundC = mapChar.find(c) != mapChar.end();
            bool foundW = mapWord.find(w) != mapWord.end();
            
            if (!foundC) {
               if (foundW) {
                   return false;
               } else {
                   mapChar[c] = w;
                   mapWord[w] = c;
               }
            } else {
                string mappedWord = mapChar[c];
                if (mappedWord != w) {
                    return false;
                }
            }
        }

        return true;
    }

private:
    vector<string> split(const string& s) {
        string tmp;
        
        vector<string> words;
        stringstream ss(s);
        
        while(getline(ss, tmp, ' ')) {
            words.push_back(tmp);
        }
        
        return words;
    }
};
