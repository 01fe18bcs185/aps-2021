# Input: Vertices=4, Edges=[3, 2], [3, 0], [2, 0], [2, 1]
# Output: Following are the two valid topological sorts for the given graph:
# 1) 3, 2, 0, 1
# 2) 3, 2, 1, 0

from collections import defaultdict as dd
from collections import deque
def solve(vertex, edges):
    if vertex <= 0:
        return []
    
    sorted_order = []

    graph = dd(list)
    indegree = dd(int)

    for v in range(vertex):
        indegree[v] = 0
    
    for v1, v2 in edges:
        graph[v1].append(v2) 
        indegree[v2] += 1
    
    source = deque()

    for v,ind in indegree.items():
        if ind == 0:
            source.append(v)

   
    while source:
        popped_vertex = source.popleft()
        sorted_order.append(popped_vertex)

        for neighbour in graph[popped_vertex]:
            indegree[neighbour] -= 1
            if indegree[neighbour] == 0:
                source.append(neighbour)
    
    if len(sorted_order) == vertex: 
        return sorted_order

    return []

print(solve(7, [[6, 2], [5, 3], [5, 4], [3, 0], [3, 1], [3, 2], [4, 1]])) 