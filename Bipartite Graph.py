'''
Ex-1
input: 
0---1
|\  |
| \ |
|  \| 
3---2

output:
False

Ex-2
input:
0---1
|   |
|   |
|   | 
3---2

output:
True
Explanation: We can partition the nodes into two sets: {0, 2} and {1, 3}.

'''

from collections import deque, defaultdict

def isBipartite(graph):
    seen = defaultdict(int)  # node:color
    
    def bfs(node):
        q = deque()
        q.append(node)
        
        while q:
            node = q.popleft()
            for nei in graph[node]:
                if nei not in seen:
                    seen[nei] = seen[node] ^ 1 # assign a color diff from parent
                    q.append(nei)
                elif seen[nei] == seen[node]: # Both belong to same set
                    return False
        return True
    
    for node in range(len(graph)):
        if node not in seen:
            seen[node] = 0
            if bfs(node) == False:
                return False
    
    return True
        
print(isBipartite([[1,3],[0,2],[1,3],[0,2]]))

