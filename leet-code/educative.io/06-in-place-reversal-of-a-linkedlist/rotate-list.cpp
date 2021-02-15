// https://leetcode.com/problems/rotate-list/

using namespace std;

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

struct ListNode {
    int val;
    ListNode *next;
};

class Solution {
public:
    ListNode* rotateRight(ListNode* head, int k) {
        if (head == nullptr || head->next == nullptr || k <= 0) {
            return head;
        }
        
        // find the length and the last node of the list
        ListNode *lastNode = head;
        int listLength = 1;
        while (lastNode->next != nullptr) {
            lastNode = lastNode->next;
            listLength++;
        }
        
        // no need to do rotation; if k is equal to list length
        // because after rotation if will comes back to the original
        if (k == listLength) {
            return head;
        }

        // connect the last node with the head to make it a circular list
        lastNode->next = head;

        // no need to do rotations more than the length of the list
        // I.e. if the length is 3 and rotate 4 means it is the same as rotate 1.
        k %= listLength;

        // length to skip from original head; to the new head after rotation
        int skipLength = listLength - k;
        
        /*
         * So what to do now is simple, we move the lastNodeOfRotatedList to the node just behind
         * the new head; after that
         *   - set the head as the lastNodeOfRotatedList->next (so it becomes the first)
         *   - set lastNodeOfRotatedList->next to null (so it becomes the last)
         */
        ListNode *lastNodeOfRotatedList = head;
        for (int i = 0; i < skipLength - 1; i++) {
            lastNodeOfRotatedList = lastNodeOfRotatedList->next;
        }
        // 'lastNodeOfRotatedList->next' is now pointing to the new head (start of the list)
        head = lastNodeOfRotatedList->next;
        lastNodeOfRotatedList->next = nullptr;
        
        return head;
    }
};
