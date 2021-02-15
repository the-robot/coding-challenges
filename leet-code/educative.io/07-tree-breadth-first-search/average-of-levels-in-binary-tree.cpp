// https://leetcode.com/problems/average-of-levels-in-binary-tree/

using namespace std;

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
    vector<double> averageOfLevels(TreeNode* root) {
        vector<double> result;
        if (root == nullptr) {
            return result;
        }
        
        // add the root into queue
        queue<TreeNode *>queue;
        queue.push(root);
        
        while (!queue.empty()) {
            int levelSize = queue.size();
            double sum = 0.0;
            
            for (int i = 0; i < levelSize; i++) {
                TreeNode *currentNode = queue.front();
                queue.pop();
                
                // sum the node value
                sum += currentNode->val;
                
                // insert the children of current node in the queue
                if (currentNode->left != nullptr) {
                    queue.push(currentNode->left);
                }
                if (currentNode->right != nullptr) {
                    queue.push(currentNode->right);
                }
            }
            result.push_back(sum / levelSize);
        }
        
        return result;
    }
};
