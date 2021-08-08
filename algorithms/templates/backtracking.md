# Backtracking

```
a. Base Case
b. Recursion Block
c. Restore (pop) Block
```

So in general, backtracking should have those 3 blocks in a solution. For example, the solution below is for the [Combinations] problem on leetcode.

```py
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.N = n
        self.K = k
        
        # store all possible combination elements
        self.nums = []
        for i in range(1, n + 1):
            self.nums.append(i)
        
        self.subsets = []

        # do backtracking        
        self.backtrack(0, [])
        
        return self.subsets
        
    def backtrack(self, index: int, subset: List[int]):
        # a. base case
        if len(subset) == self.K:
            self.subsets.append(subset[:])
            return
        
        # b. recursive calls
        #    as long as current index is not out of bound, we do backtrack
        if index < self.N:
            # do backtracking without current index
            self.backtrack(index + 1, subset)

            # do backtracking with current index
            subset.append(self.nums[index])
            self.backtrack(index + 1, subset)
            
            # c. popback the current index, so get back original subset
            subset.pop()

```
