'''
input:
  0
  |  \
  v    >
  1 ->  2
  
output: false
  
'''

def hasCycle(self, N, edges):
    #white = not visited, black = visited, grey = being visited
    adjacecy_list ={}
    visited = {}

    for vertex in range(N):
        adjacecy_list[vertex] = []
        visited[vertex] = 'white'
    
    for edge in edges:
        v1 = edge[0]
        v2 = edge[1]

        adjacecy_list[v1].append(v2)

    #Returns True if cycle detected and vice versa
    def dfs(vertex):
        visited[vertex] = 'grey'

        for neighbour in adjacecy_list[vertex]:
            if visited[neighbour] == 'grey':
                return True
            if visited[neighbour] == 'white' and dfs(neighbour):
                return True
        
        visited[vertex] = 'black' #Done
        return False

    for vertex in range(N):
        if visited[vertex] == 'white':
            if dfs(vertex):
                return True

    return False
    
print(hasCycle(4, [[0, 1], [0, 2], [1, 2]]))
