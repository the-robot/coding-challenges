from collections import deque

# This template is based on https://leetcode.com/problems/course-schedule/ as an example

"""
Example Data:

Below is bi-direction graph data.

total_nodes = 2
edges = [[1, 0], [0, 1]]
"""

def topological_sort(total_nodes: int, edges: List[List[int]]):
  # a. Initialize graph
  in_degree = {i: 0 for i in range(total_nodes)} # keep track of incoming edges
  graph = {i: [] for i in range(total_nodes)}    # adjancy list graph (keep track of child nodes)
  
  # b. Build graph
  for edge in edges:
    # n1 is parent, and n2 is child if uni-direction
    n1, n2 = edge[0], edge[1]
    
    # if bi-direction, you need to add n1 to n2 and also n2 to n1
    
    # if uni-direction, just add n2 to n1, assumed that parent points to child
    # if uni-direction, and child point to parent, you need to do the opposite for the below code
    
    in_degree[n2] += 1
    graph[n1].append(n2)
 
  # c. Find Source (starting parents)
  #    this part depends on solution, sometimes you need to find leaves
  #
  #    For example, if child points to the parent, parent would be the node that has no in-degree
  sources = deque()
  for node, degree in in_degree.items():
    if degree == 0:
      sources.append(node)
  
  # d. Remove parents or leaves, this part also depends on the question
  topological_sorted = []
  
  while sources:
    node = sources.popleft()
    
    topological_sorted.append(node)
    
    for child in graph[node]:
      inDegree[child] -= 1 # because parent is removed, so it loses one in-degree
      
      # if no one is pointing to them, anymore they becomes parent
      if inDegree[child] == 0:
        sources.append(child)
   
  # e. return something depends on question
  return ...
