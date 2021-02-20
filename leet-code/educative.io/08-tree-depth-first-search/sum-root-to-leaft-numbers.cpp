// https://leetcode.com/problems/sum-root-to-leaf-numbers/

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
    int sumNumbers(TreeNode* root) {
        return findRootToLeafPathNumbers(root, 0);
    }

private:
    static int findRootToLeafPathNumbers(TreeNode* root, int pathSum) {
        if (root == nullptr) {
            return 0;
        }

        // calculate the path number of the current node
        // it is basically concating '1' + '7' -> 17
        // you can also get that by 1 * 10 + 7 -> 17
        pathSum = 10 * pathSum + root->val;

        // if current node is a leaf; return the current path sum
        if (root->left == nullptr && root->right == nullptr) {
            return pathSum;
        }
        // traverse left and right sub-tree
        return findRootToLeafPathNumbers(root->left, pathSum) +
               findRootToLeafPathNumbers(root->right, pathSum);
    }

    static void printPath(vector<int> &path) {
        // for printing out path to debug
        for (int i = 0; i < path.size(); ++i) {
            cout << path[i] << " ";
        }
        cout << endl;
    }
};