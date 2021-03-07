// https://www.educative.io/module/lesson/patterns-for-coding-questions/RLo6pMGN1Zq

using namespace std;

#include <iostream>
#include <queue>

class TreeNode {
public:
    int val = 0;
    TreeNode *left;
    TreeNode *right;
    TreeNode *next;

    TreeNode(int x) {
        val = x;
        left = right = next = nullptr;
    }

    // tree traversal using 'next' pointer
    virtual void printTree() {
        TreeNode *current = this;
        cout << "Traversal using 'next' pointer: ";
        while (current != nullptr) {
            cout << current->val << " ";
            current = current->next;
        }
        cout << endl;
    }
};

class ConnectAllSiblings {
public:
    static void connect(TreeNode *root) {
        if (root == nullptr) {
            return;
        }
        
        TreeNode *previousNode = nullptr;
        queue<TreeNode *> queue;
        queue.push(root);
        
        while (!queue.empty()) {
            int levelSize = queue.size();

            // connect all nodes for this level
            for (int i = 0; i < levelSize; i++) {
                TreeNode *currentNode = queue.front();
                queue.pop();
                
                if (previousNode != nullptr) {
                    previousNode->next = currentNode;
                }
                previousNode = currentNode;

                // insert the child of current node in the queue
                if (currentNode->left != nullptr) {
                    queue.push(currentNode->left);
                }
                if (currentNode->right != nullptr) {
                    queue.push(currentNode->right);
                }
            }
        }
    }
};

int main() {
    TreeNode *root = new TreeNode(12);
    root->left = new TreeNode(7);
    root->right = new TreeNode(1);
    root->left->left = new TreeNode(9);
    root->right->left = new TreeNode(10);
    root->right->right = new TreeNode(5);
    ConnectAllSiblings::connect(root);
    root->printTree();
}
