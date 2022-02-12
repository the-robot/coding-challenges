# https://leetcode.com/problems/course-schedule/

from collections import deque
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        sortedOrder = []
        if numCourses <= 0:
            return True
        
        # a. initialize the graph
        inDegree = {i: 0 for i in range(numCourses)}
        graph = {i: [] for i in range(numCourses)}
        
        # b. build the graph
        for courses in prerequisites:
            parent, child = courses[0], courses[1]
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

        return len(sortedOrder) == numCourses
