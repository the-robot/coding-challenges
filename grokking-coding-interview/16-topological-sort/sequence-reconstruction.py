# https://www.lintcode.com/problem/sequence-reconstruction/

from collections import deque
from typing import List

from collections import deque
from typing import List

class Solution:
    """
    @param org: a permutation of the integers from 1 to n
    @param seqs: a list of sequences
    @return: true if it can be reconstructed only one or false
    """
    def sequenceReconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:
        # write your code here
        sortedOrder = []
        if len(org) == 0:
            return True

        # a. Initialize the graph
        inDegree = {} # count of incoming edges
        graph = {}
        for sequence in seqs:
            for num in sequence:
                inDegree[num] = 0
                graph[num] = []

        # b. Build the graph
        for sequence in seqs:
            for i in range(1, len(sequence)):
                parent, child = sequence[i-1], sequence[i]
                graph[parent].append(child)
                inDegree[child] += 1

        # if we don't have ordering rules for all the numbers we'll not be able to uniquely construct the sequence
        if len(inDegree) != len(org):
            return False

        # c. Find all sources i.e., all vertices with 0 in-degree
        sources = deque()
        for key in inDegree:
            if inDegree[key] == 0:
                sources.append(key)

        # d. For each source, add it to the sortedOrder and subtract one from all of its children's in degree
        #    if a child's in-degree becoems zero, add it to the sources queue
        while sources:
            # more than one source means, there's more than one way to reconstruct the sequence
            if len(sources) > 1:
                return False
            
            # the next source (or number) is different from the original sequence
            if org[len(sortedOrder)] != sources[0]:
                return False

            vertex = sources.popleft()
            sortedOrder.append(vertex)

            for child in graph[vertex]:
                inDegree[child] -= 1
                if inDegree[child] == 0:
                    sources.append(child)

        # if sortedOrder's size is not equal to the original sequence's size, there's no unique
        # way to construct a sequence
        return len(sortedOrder) == len(org)
