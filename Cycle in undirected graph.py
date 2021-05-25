def hasCycle(N, edges):
    adjacency_list = {}
    visited = {}

    for vertex in range(N):
        adjacency_list[vertex] = []
        visited[vertex] = False
    
    for v1,v2 in edges:
        adjacency_list[v1].append(v2)
        adjacency_list[v2].append(v1)
        
    def dfs(vertex, parent): #returns T if cycle detected and vice versa
        visited[vertex] = True

        for neighbour in adjacency_list[vertex]:
            if not visited[neighbour]:
                if dfs(neighbour, vertex):
                    return True
            else:
                if neighbour != parent:
                    return True
        return False

    for vertex in range(N):
        if not visited[vertex]:
            if dfs(vertex,-1):
                return True
    return False

print(hasCycle(4, [[1, 0], [0, 3], [1, 2], [2, 3]]))


