# https://www.educative.io/courses/grokking-the-coding-interview/q2YmVjQMMr3

from collections import deque
from typing import Dict, List


class Solution:
    def printOrders(self, tasks: int, prerequisites: List[List[int]]):
        sortedOrder = []
        if tasks <= 0:
            return True
        
        # a. initialize the graph
        inDegree = {i: 0 for i in range(tasks)}
        graph = {i: [] for i in range(tasks)}
        
        # b. build the graph
        for prerequisite in prerequisites:
            parent, child = prerequisite[0], prerequisite[1]
            graph[parent].append(child)
            inDegree[child] += 1 # increment the child in degree
        
        # c. find all sources, i.e. all vertices with 0 in-degree
        sources = deque()
        for key in inDegree:
            if inDegree[key] == 0:
                sources.append(key)
        
        self.printAllTopologicalSorts(graph, inDegree, sources, sortedOrder)

    def printAllTopologicalSorts(self, graph: Dict, inDegree: List, sources: List, sortedOrder: List):
        # for each source, add it to the sortedOrder and subtract one from all of its children's
        # in-degree if a child's in-degree becomes zero, add it to the source queue
        if sources:
            for vertex in sources:
                sortedOrder.append(vertex)
                sourcesForNextCall = deque(sources) # make a copy of sources

                # only remove the current source, all other sources should remain in the
                # queue for next call
                sourcesForNextCall.remove(vertex)

                # get the node's children to decrement their in-degrees
                for child in graph[vertex]:
                    inDegree[child] -= 1
                    if inDegree[child] == 0:
                        sourcesForNextCall.append(child)

                # recursive call to print other orderings from the remaining (and new) sources
                self.printAllTopologicalSorts(graph, inDegree, sourcesForNextCall, sortedOrder)

                # backtrack, remove the vertex from the sorted order and put all of its children back to graph
                # for the next source
                sortedOrder.remove(vertex)
                for child in graph[vertex]:
                    inDegree[child] += 1

        # topological sort is not possible as the graph has a cycle, else print sorted order
        if len(sortedOrder) == len(inDegree):
            print(sortedOrder)


if __name__ == "__main__":
    s = Solution()

    print("Task Orders:")
    s.printOrders(3, [[0, 1], [1, 2]])

    print("Task Orders:")
    s.printOrders(4, [[3, 2], [3, 0], [2, 0], [2, 1]])

    print("Task Orders:")
    s.printOrders(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]])
