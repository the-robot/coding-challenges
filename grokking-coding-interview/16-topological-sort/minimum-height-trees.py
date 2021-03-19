# https://leetcode.com/problems/minimum-height-trees/

from collections import deque
from typing import List

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 0:
            return []
        
        # with only one node, since it's in-degree will be 0, therefore, we need to handle it separately
        if n == 1:
            return [0]

        # a. Initialize the graph
        inDegree = {i: 0 for i in range(n)}  # count of incoming edges
        graph = {i: [] for i in range(n)} # adjancy list graph

        # b. Build the graph
        for edge in edges:
            n1, n2 = edge[0], edge[1]
            
            # since this is an undirected graph, therefore, add a link for both the nodes
            graph[n1].append(n2)
            graph[n2].append(n1)
            
            # increment the in-degree of both the nodes
            inDegree[n1] += 1
            inDegree[n2] += 1
        
        # c. Find all leaves i.e., all nodes with 0 in-degrees
        leaves = deque()
        for key in inDegree:
            if inDegree[key] == 1:
                leaves.append(key)

        # d. Remove leaves level by level and subtract each leave's children's in-degree.
        #    Repeat this until we are left with 1 or 2 nodes, which will be our answer.
        #    Any node that has always been a leaf cannot be the root of a minimum heaigh tree, because
        #    its adjacent non-leaf node will always be a better candidate.
        totalNodes = n
        while totalNodes > 2:
            leaveSize = len(leaves)
            totalNodes -= leaveSize
            
            for i in range(0, leaveSize):
                vertex = leaves.popleft()
                
                # get the node's children to decrement their in-degree
                for child in graph[vertex]:
                    inDegree[child] -= 1
                    if inDegree[child] == 1:
                        leaves.append(child)

        return list(leaves)
