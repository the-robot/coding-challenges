// https://leetcode.com/problems/path-sum-ii/

using namespace std;

#include <iostream>
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
    vector<vector<int>> pathSum(TreeNode* root, int targetSum) {
        vector<vector<int>> allPaths;
        vector<int> currentPath;
        findPathsRecursive(root, targetSum, currentPath, allPaths);
        return allPaths;
    }
    
private:
    static void findPathsRecursive(
        TreeNode* root, int sum, vector<int> &currentPath, vector<vector<int>> &allPath
    ) {
        if (root == nullptr) {
            return;
        }
        
        // add the current node to the path
        currentPath.push_back(root->val);
        
        // if the current nodei s a leaf and it's value is equal to sum, save the current path
        if (root->val == sum && root->left == nullptr && root->right == nullptr) {
            allPath.push_back(vector<int>(currentPath));
        } else {
            // traverse the left sub-tree
            findPathsRecursive(root->left, sum - root->val, currentPath, allPath);
            
            // traverse the right sub-tree
            findPathsRecursive(root->right, sum - root->val, currentPath, allPath);
        }
        
        // remove the current node from the path of backtrack,
        // we need to remove the current node while we are going up the recursive call stack.
        currentPath.pop_back();
    }

    static void printPath(vector<int> &path) {
        // for printing out path to debug
        for (int i = 0; i < path.size(); ++i) {
            cout << path[i] << " ";
        }
        cout << endl;
    }
};
