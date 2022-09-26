from collections import *
def dfs(vertices, edges, source):
    adj = {i:[] for i in range(vertices)}
    
    for parent, child in edges:
        adj[parent] += [child]

    stack = deque()
    stack.append(source)

    while stack:
        currentNode = stack.popleft()
        print(currentNode)
        children = adj.get(currentNode, 0)
        if children:
            for child in children:
                stack.append(child)
        
dfs(5, [[1,2], [2,4], [1,3], [3,5], [3,6]], 1)