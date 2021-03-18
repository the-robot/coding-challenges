# https://www.educative.io/courses/grokking-the-coding-interview/m25rBmwLV00

from collections import deque
from typing import List

class Solution:
    def sort(self, vertices: int, edges: List[List[int]]) -> List[int]:
        sortedOrder = []
        if vertices <= 0:
            return sortedOrder

        # a. initialize the graph
        inDegree = {i: 0 for i in range(vertices)} # count of incoming edges (parents)
        graph = {i: [] for i in range(vertices)} # adjacency list graph (number of childrens below)

        # b. build the graph
        for edge in edges:
            parent, child = edge[0], edge[1]
            graph[parent].append(child)
            inDegree[child] += 1 # increment of child in degree

        # c. find all sources i.e., all vertices with 0 in-degree
        sources = deque()
        for key in inDegree:
            # add verticies to source that has no parent above
            if inDegree[key] == 0:
                sources.append(key)

        # d. for each source, add it to the sortedOrder and subtract one from all of its children's
        #    in-degree if a child's in-degree becomes zero, add it to the source queue
        while sources:
            vertex = sources.popleft()
            sortedOrder.append(vertex)

            # get the node's children to decrement their in-degree
            for child in graph[vertex]:
                inDegree[child] -= 1
                if inDegree[child] == 0:
                    sources.append(child)

        # topological sort is not possible as the graph has a cycle
        if len(sortedOrder) != vertices:
            return []

        return sortedOrder


if __name__ == "__main__":
    s = Solution()

    print(s.sort(4, [[3, 2], [3, 0], [2, 0], [2, 1]]))
    print(s.sort(5, [[4, 2], [4, 3], [2, 0], [2, 1], [3, 1]]))
    print(s.sort(7, [[6, 4], [6, 2], [5, 3], [5, 4], [3, 0], [3, 1], [3, 2], [4, 1]]))
