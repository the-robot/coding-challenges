// https://leetcode.com/problems/path-sum-iii/

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
    int pathSum(TreeNode* root, int sum) {
        vector<int> currentPath;
        return countPathsRecursive(root, sum, currentPath);
    }
    
private:
    static int countPathsRecursive(TreeNode *currentNode, int S, vector<int> &currentPath) {
        if (currentNode == nullptr) {
            return 0;
        }
        
        // add the current node to the path
        currentPath.push_back(currentNode->val);
        int pathCount = 0, pathSum = 0;
        // find the sum of all sub-paths in the current path list
        for (vector<int>::reverse_iterator itr = currentPath.rbegin(); itr != currentPath.rend(); ++itr) {
            pathSum += *itr;
            // if the sum of any sub-path is equal to 'S' we increment our path count.
            if (pathSum == S) {
                pathCount++;
            }
        }
        
        // traverse the left sub-tree
        pathCount += countPathsRecursive(currentNode->left, S, currentPath);
        // traverse the right sub-tree
        pathCount += countPathsRecursive(currentNode->right, S, currentPath);
        
        // remove the current node from the path to backtrack,
        // we need to remove the current node while we are going up the recursive call stack.
        currentPath.pop_back();
        
        return pathCount;
    }
    
    static void printArray(vector<int> &current) {
        for (int i = 0; i < current.size(); ++i) {
            cout << current[i] << " ";
        }
        cout << endl;
    }
};
