// https://www.educative.io/module/lesson/data-structures-in-python/qVEMgx4xYr3

using namespace std;

#include <iostream>

class ListNode {
public:
    int value = 0;
    ListNode *next;

    ListNode(int value) {
        this->value = value;
        this->next = nullptr;
    }
};

class ReverseAlternatingKElements {
public:
    static ListNode *reverse(ListNode *head, int k) {
        if (k <= 1 || head == nullptr) {
            return head;
        }

        ListNode *current = head, *previous = nullptr;
        while (true) {
            ListNode *lastNodeOfPreviousPart = previous;
            // after reversing the LinkedList current will become lastnode of the sublist
            ListNode *lastNodeOfSubList = current;
            ListNode *next = nullptr; // will be used to temporarily store the next node

            // reverse 'k' nodes
            for (int i = 0; current != nullptr && i < k; i++) {
                next = current->next;
                current->next = previous;
                previous = current;
                current = next;
            }

            // connect with the previous part
            if (lastNodeOfPreviousPart != nullptr) {
                // previous is now the first node of the sublist
                lastNodeOfPreviousPart->next = previous;
            } else {
                head = previous;
            }

            // connect with the next part
            lastNodeOfSubList->next = current;

            // skip 'k' nodes
            for (int i = 0; current != nullptr && i < k; i++) {
                previous = current;
                current = current->next;
            }

            // if no more nodes at the current position
            if (current == nullptr) {
                break;
            }
        }

        return head;
    }
};

int main() {
    ListNode *head = new ListNode(1);
    head->next = new ListNode(2);
    head->next->next = new ListNode(3);
    head->next->next->next = new ListNode(4);
    head->next->next->next->next = new ListNode(5);
    head->next->next->next->next->next = new ListNode(6);
    head->next->next->next->next->next->next = new ListNode(7);
    head->next->next->next->next->next->next->next = new ListNode(8);

    ListNode *result = ReverseAlternatingKElements::reverse(head, 2);
    cout << "Nodes of the reversed LinkedList are: ";
    while (result != nullptr) {
        cout << result->value << " ";
        result = result->next;
    }
    cout << endl;
}
