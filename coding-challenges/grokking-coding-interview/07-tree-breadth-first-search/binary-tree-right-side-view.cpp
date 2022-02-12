// https://leetcode.com/problems/binary-tree-right-side-view/

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

class TreeNode {
public:
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode* next;
};

class Solution {
public:
    vector<int> rightSideView(TreeNode* root) {
        vector<int> result = {};
        if (root == nullptr) {
            return result;
        }
        
        queue<TreeNode *> queue;
        queue.push(root);
        
        while (!queue.empty()) {
            int levelSize = queue.size();
            
            // connect all nodes for this level
            for (int i = 0; i < levelSize; i++) {
                TreeNode *currentNode = queue.front();
                queue.pop();

                // insert the child of current node in the queue
                if (currentNode->left != nullptr) {
                    queue.push(currentNode->left);
                }
                if (currentNode->right != nullptr) {
                    queue.push(currentNode->right);
                }
                
                // if i is last node of the level; add to result
                if (i == (levelSize - 1)) {
                    result.push_back(currentNode->val);
                }
            }
        }
        
        return result;
    }
};
