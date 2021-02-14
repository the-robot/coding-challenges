// https://leetcode.com/problems/reverse-linked-list-ii/

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
    ListNode* reverseBetween(ListNode* head, int m, int n) {
        if (m == n) {
            return head;
        }
        
        ListNode *current = head;
        ListNode *previous = nullptr;

        // skip m-1 nodes
        for (int i = 0; current != nullptr && i < m - 1; i++) {
            previous = current;
            current = current->next;
        }
        
        // the node after n
        ListNode *lastNodeOfFirstPart = previous;
        
        // after reversing; last node of sublist will be current
        ListNode *lastNodeOfSubList = current;
        ListNode *next = nullptr;
        
        // reverse until n
        for (int i = 0; current != nullptr && i < k; i++) {
            next = current->next;
            current->next = previous;
            previous = current;
            current = next;
        }
        
        // connect with the first part
        if (lastNodeOfFirstPart != nullptr) {
            lastNodeOfFirstPart->next = previous; // previous is now the first node of sublist
        } else {
            head = previous;
        }
        
        // connect to the last part
        lastNodeOfSubList->next = current;
        
        return head;
    }
};
