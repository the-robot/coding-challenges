//https://leetcode.com/problems/binary-tree-level-order-traversal-ii/

using namespace std;

#include <deque>
#include <queue>
#include <vector>

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
};

class Solution {
public:
    vector<vector<int>> levelOrderBottom(TreeNode* root) {
        deque<vector<int>> dResult;
        vector<vector<int>> result;
        if (root == nullptr) {
            return result;
        }
        
        // add the root into queue
        queue<TreeNode *> queue;
        queue.push(root);
        
        while (!queue.empty()) {
            int levelSize = queue.size();
            vector<int> currentLevel;
            
            for (int i = 0; i < levelSize; i++) {
                TreeNode *currentNode = queue.front();
                queue.pop();
                
                // add the node to the current level
                currentLevel.push_back(currentNode->val);
                
                // insert the children of current node in the queue
                if (currentNode->left != nullptr) {
                    queue.push(currentNode->left);
                }
                if (currentNode->right != nullptr) {
                    queue.push(currentNode->right);
                }
            }
            dResult.push_front(currentLevel);
        }
        
        // convert deque to vector
        while (!dResult.empty()) {
            result.push_back(dResult.front());
            dResult.pop_front();
        }
        
        return result;
    }
};
