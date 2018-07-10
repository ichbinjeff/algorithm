def _build_graph(pairs, degree):
	graph = {}

	for i in xrange(len(pairs)):
		parent = pairs[i][0]
		child = pairs[i][1]
		
		if parent not in degree:
			degree[parent] = 0
		if child not in degree:
			degree[child] = 0
		degree[child] += 1

		if parent not in graph:
			graph[parent] = [child]
		else:
			graph[parent].append(child)
	
	return graph

def parent_child(pairs):
	degree = {}
	graph = _build_graph(pairs, degree)
	rst = [[], []]
	for k in degree:
		if degree[k] == 0:
			rst[0].append(k)
		elif degree[k] == 1:
			rst[1].append(k)
	return rst

def has_common_ancester(p, q, pairs):
	degree = {}
	graph = _build_graph(pairs, degree)
	roots = []

	for k in degree:
		if degree[k] == 0:
			roots.append(k)

	pathP = []
	pathQ = []
	visited = set()
	for r in roots:
		find_path(pathP, [], r, p, graph, visited)

	for r in roots:
		find_path(pathQ, [], r, q, graph, visited)

	for val in set(pathP):
		if val in pathQ:
			return True
	
	return False

def find_path(rst, level, currNode, target, graph, visited):
	if currNode == target:
		rst.extend(level[:])
		return 

	if currNode in graph:
		visited.add(currNode)
		level.append(currNode)
		for neighbor in graph[currNode]:
			if neighbor not in visited:
				find_path(rst, level, neighbor, target, graph, visited)
		level.pop()
		visited.remove(currNode)

print has_common_ancester(3, 9, [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9)])
