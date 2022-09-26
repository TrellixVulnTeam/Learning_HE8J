```python
def toposort(vertices, edges):
	sortedOrder = []
	if vertices <= 0:
		return sortedOrder
	#intialise the graph
	inDegree = {i: 0 for i in range(vertices)}
	graph = {i: [] for i in range(vertices)}
	
	#build the graph
	for edge in edges:
		parent, child = edge[0], edge[1]
		graph[parent].append(child)
		inDegree[child] += 1
	
	#find all sources
	sources = deque()
	for key in inDegree:
		if inDegree[key] == 0:
			sources.append(key)
	
	#for each source, add it to sorted order, if child indegree becomes zero, add to sources
	while sources:
		vertex = sources.popLeft()
		sortedOrder.append(vertex)
	
		for child in graph[vertex]:
			inDegree[child] -= 1
	
		if inDegree[child] == 0:
			sources.append(child)
	
	
	if len(sortedOrder) != vertices:
		return []
	
		return sortedOrder

```