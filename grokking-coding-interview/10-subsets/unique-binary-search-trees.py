# https://leetcode.com/problems/unique-binary-search-trees/

# https://www.youtube.com/watch?v=Ox0TenN3Zpg
# https://leetcode.com/problems/unique-binary-search-trees/discuss/703644/PythonEasy-DP-Solution-Explained-By-Someone-Who-Used-To-Struggle-To-Understand-DP
class Solution:
    def numTrees(self, n: int) -> int:
        # i.e. n = 3 [1, -1, -1, -1]
        self.table = [-1] * (n + 1)
        self.table[0] = 1 # n = 0 has only root node, 1

        return self.numTreesRec(n)

    def numTreesRec(self, n: int) -> int:
        # if not -1, we have seen the number before so just return
        if self.table[n] != -1:
            return self.table[n]

        total = 0
        for m in range(n):
            total += (self.numTreesRec(n-1-m) * self.numTreesRec(m))

        self.table[n] = total
        return total
