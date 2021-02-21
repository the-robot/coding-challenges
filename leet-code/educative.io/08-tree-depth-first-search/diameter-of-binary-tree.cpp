// https://leetcode.com/problems/diameter-of-binary-tree/

using namespace std;

#include <algorithm>

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
    int diameterOfBinaryTree(TreeNode* root) {
        int treeDiameter = 0;
        calculateHeight(root, treeDiameter);
        return treeDiameter;
        
    }

private:
    static int calculateHeight(TreeNode* currentNode, int &treeDiameter) {
        if (currentNode == nullptr) {
            return 0;
        }
        
        int leftTreeHeight = calculateHeight(currentNode->left, treeDiameter);
        int rightTreeHeight = calculateHeight(currentNode->right, treeDiameter);
        
        // diameter at the current node will be equal to the height of left subtree +
        // the height of right subtree
        int diameter = leftTreeHeight + rightTreeHeight;
        
        // update the global tree diameter
        treeDiameter = max(treeDiameter, diameter);
        
        // height of the current node will be equal to the maximum of the heights of
        // left or right subtree plus '1' for the current node
        return max(leftTreeHeight, rightTreeHeight) + 1;
    }
};
