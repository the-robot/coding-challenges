Useful when dealing with cyclic linked lists or array.

**Ways to identify when to use the Fast and Slow pattern:**

- The problem will deal with a loop in a linked list, array or sometimes a single number (`Happy Number` problem)
- When you need to know the position of a certain element or the overall length of the linked list.

<br/>

> When should I use it over the Two Pointer method mentioned above?  
> 
> There are some cases where you shouldn’t use the Two Pointer approach such as in a singly linked list where you can’t move in a backwards direction. An example of when to use the Fast and Slow pattern is when you’re trying to determine if a linked list is a palindrome.  

Problems featuring the fast and slow pointers pattern:  
- Linked List Cycle (easy)
- Palindrome Linked List (medium)
- Cycle in a Circular Array (hard)

<br/>

**Problem Alternatives**

| Date | Name | Difficulty | Solution |
|:----:|:-----|:----------:|:--------:|
| Feb, 07, 2021 | [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) | Easy | [.go](https://github.com/the-robot/coding-challenges/blob/master/leet-code/educative.io/03-fast-and-slow-pointers/linked-list-cycle.go) |
| | [Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/) | Medium | [.go](https://github.com/the-robot/coding-challenges/blob/master/leet-code/educative.io/03-fast-and-slow-pointers/linked-list-cycle-ii.go) |
| | [Happy Number](https://leetcode.com/problems/happy-number/) | Easy | [.go](https://github.com/the-robot/coding-challenges/blob/master/leet-code/educative.io/03-fast-and-slow-pointers/happy-number.go) |
| | [Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/) | Easy | [.go](https://github.com/the-robot/coding-challenges/blob/master/leet-code/educative.io/03-fast-and-slow-pointers/middle-of-the-linked-list.go) |
| | [Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/) | Easy | [.go](https://github.com/the-robot/coding-challenges/blob/master/leet-code/educative.io/03-fast-and-slow-pointers/palindrome-linked-list.go) |
| | [Reorder List](https://leetcode.com/problems/reorder-list/description/) | Medium | [.go](https://github.com/the-robot/coding-challenges/blob/master/leet-code/educative.io/03-fast-and-slow-pointers/reorder-list.go) |