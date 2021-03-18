# https://www.educative.io/courses/grokking-the-coding-interview/q2YmVjQMMr3

from collections import deque
from typing import List


# TODO:
class Solution:
    def printOrders(self, numCourses: int, prerequisites: List[List[int]]):
        sortedOrder = []
        if numCourses <= 0:
            return True
        
        # a. initialize the graph
        inDegree = {i: 0 for i in range(numCourses)}
        graph = {i: [] for i in range(numCourses)}
        
        # b. build the graph
        for courses in prerequisites:
            # because course[0] depends on course[1] so course[1] is the parent
            parent, child = courses[1], courses[0]
            graph[parent].append(child)
            inDegree[child] += 1 # increment the child in degree
        
        # c. find all sources, i.e. all vertices with 0 in-degree
        sources = deque()
        for key in inDegree:
            if inDegree[key] == 0:
                sources.append(key)
        
        # d. for each source, add it to the sortedOrder and subtract one from all of its children's
        #    in-degree if a child's in-degree becomes zero, add it to the source queue
        while sources:
            vertex = sources.popleft()
            sortedOrder.append(vertex)
            
            for child in graph[vertex]:
                inDegree[child] -= 1
                if inDegree[child] == 0:
                    sources.append(child)

        # topological sort is not possible as the graph has a cycle
        if len(sortedOrder) != numCourses:
            return []

        return sortedOrder


if __name__ == "__main__":
    s = Solution()

    print("Task Orders:")
    s.printOrders(3, [[0, 1], [1, 2]])

    print("Task Orders:")
    s.printOrders(4, [[3, 2], [3, 0], [2, 0], [2, 1]])

    print("Task Orders:")
    s.printOrders(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]])
