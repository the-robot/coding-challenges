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
        
        lastNode->next = head; // connect the last node with the head to make it a circular list
        k %= listLength; // no need to do ratations more than the length of the list
        int skipLength = listLength - k;
        
        ListNode *lastNodeOfRotatedList = head;
        for (int i = 0; i < skipLength - 1; i++) {
            lastNodeOfRotatedList = lastNodeOfRotatedList->next;
        }
        
        // 'lastNodeOfRotatedList->next' is pointing to the sublist of 'k' ending nodes
        head = lastNodeOfRotatedList->next;
        lastNodeOfRotatedList->next = nullptr;
        
        return head;
    }
};
