// https://www.educative.io/courses/grokking-the-coding-interview/RMZylvkGznR

using namespace std;

#include <iostream>

class ListNode {
public:
    int value = 0;
    ListNode *next;

    ListNode(int value) {
        this->value = value;
        next = nullptr;
    }
};

class ReverseEveryKElements {
public:
    static ListNode *reverse(ListNode *head, int k) {
        // TODO:
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

    ListNode *result = ReverseEveryKElements::reverse(head, 3);
    cout << "Nodes of the reversed LinkedList are: ";
    while (result != nullptr) {
        cout << result->value << " ";
        result = result->next;
    }
    cout << endl;
};
