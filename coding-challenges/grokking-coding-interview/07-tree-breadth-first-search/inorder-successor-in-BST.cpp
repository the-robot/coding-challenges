// https://www.lintcode.com/problem/inorder-successor-in-bst/

using namespace std;

#include <queue>

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
};
class Solution {
public:
    /*
     * @param root: The root of the BST.
     * @param p: You need find the successor node of p.
     * @return: Successor of p.
     */
    TreeNode * inorderSuccessor(TreeNode * root, TreeNode * p) {
        // if root is empty; no child also so return null
        if (root == nullptr) {
            return nullptr;
        }
        
        // if root is equals to key
        if (root == p) {
            // if left child exists; it will be successor
            if (root->left) {
                return root->left;
            }
            // if right child exists it will be successor
            else if (root->right) {
                return root->right;
            }
            else {
                return nullptr;
            }
        }

        queue<TreeNode *> q;
        q.push(root);
        
        while (!q.empty()) {
            TreeNode *currentNode = q.front();
            q.pop();
            
            // insert the children of current node in the queue
            if (currentNode->left != nullptr) {
                q.push(currentNode->left);
            }

            if (currentNode->right != nullptr) {
                q.push(currentNode->right);
            }
            
            // break if we found the key
            if (currentNode == p) {
                break;
            }
        }
        
        return q.front();
    }
};
