// https://leetcode.com/problems/fruit-into-baskets/

#include <vector>
#include <unordered_map>
ls
using namespace std;

class Solution {
    public:
        int totalFruit(vector<int>& tree) {
            unordered_map<int, int> basket; // <tree number : frequency>
            int maxLength = 0;
            int left = 0;
            
            for (int right = 0; right < tree.size(); right++) {
                basket[tree[right]]++;
                
                // total number of unique fruits is 2
                while ((int)basket.size() > 2) {
                    int leftFruit = tree[left];
                    basket[leftFruit]--;
                    
                    if (basket[leftFruit] == 0) {
                        basket.erase(leftFruit);
                    }
                    left++;
                }
                
                maxLength = max(maxLength, right - left + 1);
            }
            
            return maxLength;
        }
};
