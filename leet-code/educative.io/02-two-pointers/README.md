**Ways to identify when to use the Two Pointer method:**

- It will feature problems where you deal with sorted arrays (or Linked Lists) and need to find a set of elements that fulfill certain constraints
- The set of elements in the array is a pair, a triplet, or even a subarray

Here are some problems that feature the Two Pointer pattern:
- Squaring a sorted array (easy)
- Triplets that sum to zero (medium)
- Comparing strings that contain backspaces (medium)

<br/>

**Problem Alternatives**

| Date | Name | Difficulty | Solution | Is Sorted | Constraints | Type of elements to find |
|:----:|:-----|:----------:|:--------:|:---------:|:-----------:|:------------------------:|
| Feb 02, 2021 | [Two Sum](https://leetcode.com/problems/two-sum/) | Easy | [.cpp](https://github.com/the-robot/coding-challenges/blob/master/leet-code/educative.io/02-two-pointers/two-sum.cpp) | True (sort if not) | Find 2 numbers that sum of those is equal to target | 2 numbers from an array |
| Feb 03, 2021 | [Remove Duplicates from Sorted List](https://leetcode.com/problems/remove-duplicates-from-sorted-list/) | Easy | [.go](https://github.com/the-robot/coding-challenges/blob/master/leet-code/educative.io/02-two-pointers/remove-duplicates-from-sorted-list.go) | True | Remove number that appears more than once | Subarray that has no duplicate |
| | [Remove Duplicates from Sorted List II](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/) | Medium | [.go](https://github.com/the-robot/coding-challenges/blob/master/leet-code/educative.io/02-two-pointers/remove-duplicates-from-sorted-list-ii.go) | True | Remove number that has duplicate | Subarray that contains only numbers that have no duplicate in original array |
| | [Remove Duplicates from Sorted Array II](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii) | Medium | [.go](https://github.com/the-robot/coding-challenges/blob/master/leet-code/educative.io/02-two-pointers/remove-duplicates-from-sorted-array-ii.go) | True | Remove element that have duplicates | Subset (length of subset) |
| | [Squares of a Sorted Array](https://leetcode.com/problems/squares-of-a-sorted-array/) | Easy | [.go](https://github.com/the-robot/coding-challenges/blob/master/leet-code/educative.io/02-two-pointers/squares-of-a-sorted-array.go) | True | The squared number from the original must be sorted (the square of negative may be larger than square of positive `-16 vs 2`, those negative square must be on right side in answer, sorted) | Sorted array of squared number |
| | [3Sum](https://leetcode.com/problems/3sum/) | Medium | [.cpp](https://github.com/the-robot/coding-challenges/blob/master/leet-code/educative.io/02-two-pointers/3sum.cpp) | True (sort if not) | Find 3 numbers (triplet) such that sum of those 3 is equal to 0 | 3 numbers, triplet |
| | [3Sum Closest](https://leetcode.com/problems/3sum-closest/) | Medium | [.go](https://github.com/the-robot/coding-challenges/blob/master/leet-code/educative.io/02-two-pointers/3sum-closest.go) | True (sort if not) | Find 3 numbers (triplet) such that sum of those 3 is closest to the target number | 3 numbers, triplet |
| | [3Sum Smaller](https://www.lintcode.com/problem/3sum-smaller/description) | Medium | [.go](https://github.com/the-robot/coding-challenges/blob/master/leet-code/educative.io/02-two-pointers/3sum-smaller.go) | True (sort if not) | Find all possible 3 numbers such that sum of those 3 is less than the target number | Total count of how many triplets that can fulfill the constraints (aka all possible subsets from an array |
| | [4Sum](https://leetcode.com/problems/4sum/) | Medium | [.cpp](https://github.com/the-robot/coding-challenges/blob/master/leet-code/educative.io/02-two-pointers/4sum.cpp) |  True (sort if not) | Same as 3Sum | 4 numbers, quardruplets |
| Feb 04, 2021 | [Dutch national flag sorting problem](https://coderbyte.com/algorithm/dutch-national-flag-sorting-problem) | Medium | [.go](https://github.com/the-robot/coding-challenges/blob/master/leet-code/educative.io/02-two-pointers/dutch-national-flag-sorting-problem.go) | False (because we need to sort it for solution, this question is quite different from the rest) | Using 2 pointers and 1 iterator pointer, we find the number (0, 1, 2, can be different like A, B, C) and move the number according to left-right pointer for sorting | Sorted array |
| | [Backspace String Compare](https://leetcode.com/problems/backspace-string-compare/) | Easy | [.go](https://github.com/the-robot/coding-challenges/blob/master/leet-code/educative.io/02-two-pointers/backspace-string-compare.go) |
| | [Shortest Unsorted Continuous Subarray](https://leetcode.com/problems/shortest-unsorted-continuous-subarray/) | Medium | [.go](https://github.com/the-robot/coding-challenges/blob/master/leet-code/educative.io/02-two-pointers/shortest-unsorted-continuous-subarray.go) |
