// https://leetcode.com/problems/ipo/

using namespace std;

#include <queue>
#include <vector>

class Solution {
public:
    int findMaximizedCapital(int k, int W, vector<int>& Profits, vector<int>& Capital) {
        int maximumCapital = W;

        // top element = max profit among all projects
        priority_queue<int> maxProfits;
        
        // top element = min capital among all projects
        priority_queue<pair<int, int>, vector<pair<int, int> >, greater<pair<int,int> > > projects;
        
        for (int i = 0; i < Capital.size(); ++i) {
            projects.push( make_pair(Capital[i], i) );
        }
        
        for (int i = 0; i < k; ++i) {
            // push values
            while (!projects.empty() && projects.top().first <= maximumCapital) {
                maxProfits.push( Profits[projects.top().second] ); // push all the profits for which capital <= W
                projects.pop();
            }
            
            if (!maxProfits.empty()) {
                maximumCapital += maxProfits.top();
                maxProfits.pop();
            }
        }

        return maximumCapital;
    }
};
