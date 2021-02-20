// https://www.educative.io/courses/grokking-the-coding-interview/m280XNlPOkn

using namespace std;

#include <iostream>
#include <vector>

class TreeNode {
public:
    int val;
    TreeNode *left;
    TreeNode *right;

    TreeNode(int x) {
        val = x;
        left = right = nullptr;
    }
};

class PathWithGivenSequence {
public:
    static bool findPath(TreeNode *root, const vector<int> &sequence) {
        if (root == nullptr) {
            return sequence.empty();
        }

        return findPathRecursive(root, sequence, 0);
    }

private:
    static bool findPathRecursive(TreeNode *currentNode, const vector<int> &sequence, int sequenceIndex) {
        if (currentNode == nullptr) {
            return false;
        }

        if (sequenceIndex >= sequence.size() || currentNode->val != sequence[sequenceIndex]) {
            return false;
        }

        // if the current node is a leaft, and it is the end of sequence, we have found the path
        if (currentNode->left == nullptr && currentNode->right == nullptr &&
            sequenceIndex == sequence.size() - 1)
        {
            return true;
        }

        // recursively call to traverse the left and right sub-tree
        // return true if any of the two recursive call return true
        return findPathRecursive(currentNode->left, sequence, sequenceIndex + 1) ||
               findPathRecursive(currentNode->right, sequence, sequenceIndex + 1);
    }
};

int main() {
    TreeNode *root = new TreeNode(1);
    root->left = new TreeNode(0);
    root->right = new TreeNode(1);
    root->left->left = new TreeNode(1);
    root->right->left = new TreeNode(6);
    root->right->right = new TreeNode(5);

    cout << "Tree has path sequence: " << PathWithGivenSequence::findPath(root, vector<int>{1, 0, 7}) << endl;
    cout << "Tree has path sequence: " << PathWithGivenSequence::findPath(root, vector<int>{1, 1, 6}) << endl;
}
