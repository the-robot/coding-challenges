# https://www.lintcode.com/problem/alien-dictionary/
# https://evanyang.gitbooks.io/leetcode/content/LeetCode/alien_dictionary.html

from collections import deque
from typing import List

class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """
    def alienOrder(self, words: List[str]):
        # Write your code here
        if len(words) == 0:
            return ""

        # a. initialize the graph
        inDegree = {} # count the incoming edge
        graph = {} # adjancy list graph
        for word in words:
            for character in word:
                inDegree[character] = 0
                graph[character] = []

        # b. build the graph
        for i in range(0, len(words) - 1):
            # find ordering of characters from adjacent words
            w1, w2 = words[i], words[i + 1]

            for j in range(0, min(len(w1), len(w2))):
                parent, child = w1[j], w2[j]

                # if two characters are different
                # put the child into it's parent's list
                if parent != child:
                    graph[parent].append(child)
                    inDegree[child] += 1
                    break

        # c. find all sources, i.e. all vertices with 0 in degree
        sources = deque()
        for key in inDegree:
            if inDegree[key] == 0 and len(graph[key]) > 0:
                sources.append(key)

        # d. for each sources, add it to the sortedOrder and subtract one from all of
        #    its children's in-degree if a child's in-degree becomes zero, add it to
        #    the source queue
        sortedOrder = []
        while sources:
            vertex = sources.popleft()
            sortedOrder.append(vertex)

            for child in graph[vertex]:
                inDegree[child] -= 1
                if inDegree[child] == 0:
                    sources.append(child)
    
        # if sortedOrder doesn't contain all characters, there's a cyclic dependency between
        # characters, will not be able to find the correct ordering of the characters
        if len(sortedOrder) != len(inDegree):
            return ""

        return "".join(sortedOrder)
