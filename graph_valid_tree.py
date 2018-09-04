# [[0,1], [0,2], [0,3], [1,4]]
#
# 0 1,2,3
# 1 0,4
# 2 0
# 3 0
# 4 1

class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        if len(edges) != n-1:
            return False

        graph = self.build_graph(edges)
        visited = {}
        if self.has_cycle(visited, graph, graph[0]):
            return False
        for node in graph:
            if node not in visited:
                return False

        return True

    def build_graph(self, edges):
        graph = {}
        for edge in edges:
            graph[edge[0]] = edge[1]
            graph[edge[1]] = edge[0]

        return graph

    def has_cycle(self, visited, graph, parent):
        visited[parent] = True
        neighbors = graph[parent]
        for n in neighbors:
            if n in visited and n != parent:
                return True
            if self.has_cycle(visited, graph, n):
                return True
        return False
