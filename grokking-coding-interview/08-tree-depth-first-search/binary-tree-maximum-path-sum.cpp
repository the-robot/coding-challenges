// https://leetcode.com/problems/binary-tree-maximum-path-sum/

using namespace std;

#include <algorithm>
#include <limits>

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
    int maxPathSum(TreeNode* root) {
        int pathSum = numeric_limits<int>::min();
        calculateSum(root, pathSum);
        return pathSum;
    }

private:
    static int calculateSum(TreeNode *currentNode, int &pathSum) {
        if (currentNode == nullptr) {
            return 0;
        }
        
        int leftTreeSum = calculateSum(currentNode->left, pathSum);
        int rightTreeSum = calculateSum(currentNode->right, pathSum);
        
        // ignore paths with negative sum, since we are finding maximum sum
        // ignore any path with overall negative sum
        leftTreeSum = max(leftTreeSum, 0);
        rightTreeSum = max(rightTreeSum, 0);
        
        // sum at the current node will be equal to the sum of left subtree +
        // sum of right subtree
        int localSum = leftTreeSum + rightTreeSum + currentNode->val;
        
        // update global pathsum
        pathSum = max(pathSum, localSum);
        
        // sum of the current node will be equal to the maximum of the sum of
        // left or right subtree for the current node
        return max(leftTreeSum, rightTreeSum) + currentNode->val;
    }
};
