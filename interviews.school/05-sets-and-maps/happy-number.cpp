// https://leetcode.com/problems/happy-number/

#include <unordered_set>

using namespace std;

class Solution {
private:
    int sumOfSquares(int n) {
        int sum = 0;
        
        while (n > 0) {
            int digit = n % 10;
            sum += digit * digit;
            n = n / 10;
        }
        
        return sum;
    }
    
public:
    bool isHappy(int n) {
        unordered_set<int> visit;
        
        while (visit.find(n) == visit.end()) {
            visit.insert(n);
            n = this->sumOfSquares(n);
            if (n == 1) {
                return true;
            }
        }
        
        return false;
    }
};
