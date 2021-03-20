In many problems, we are given a set of elements such that we can divide them into two parts. To solve the problem, we are interested in knowing the smallest element in one part and the biggest element in the other part. This pattern is an efficient approach to solve such problems.  

This pattern uses two heaps; A Min Heap to find the smallest element and a Max Heap to find the biggest element. The pattern works by storing the first half of numbers in a Max Heap, this is because you want to find the largest number in the first half. You then store the second half of numbers in a Min Heap, as you want to find the smallest number in the second half. At any time, the median of the current list of numbers can be calculated from the top element of the two heaps.  

**Ways to identify the Two Heaps pattern:** 
- Useful in situations like Priority Queue, Scheduling.
- If the problem states that you need to find the smallest/largest/median elements of a set.
- Sometimes, useful in problems featuring a binary tree data structure.

Problems featuring:  
- Find the Median of a Number Stream (medium)

<br/>

| Date | Name | Difficulty | Solution |
|:----:|:-----|:----------:|:--------:|
| Feb, 24 2021 | [Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/) | Hard | [.cpp](https://github.com/the-robot/coding-challenges/blob/master/grokking-coding-interview/09-two-heaps/find-median-from-data-stream.cpp) |
| Feb, 25 2021 | [Sliding Window Median](https://leetcode.com/problems/sliding-window-median/) | Hard | [.cpp](https://github.com/the-robot/coding-challenges/blob/master/grokking-coding-interview/09-two-heaps/sliding-window-median.cpp) |
| Feb, 26 2021 | [IPO](https://leetcode.com/problems/ipo/) | Hard | [.cpp](https://github.com/the-robot/coding-challenges/blob/master/grokking-coding-interview/09-two-heaps/ipo.cpp) |
| Feb, 27 2021 | [Find Right Interval](https://leetcode.com/problems/find-right-interval/) | Medium | [.cpp](https://github.com/the-robot/coding-challenges/blob/master/grokking-coding-interview/09-two-heaps/find-right-interval.cpp) |
