class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        degree = {}
        for i in xrange(len(prerequisites)):
        	degree[i] = 0

        graph = self.build_graph(numCourses, degree, prerequisites)
        rst = []
        queue = []
        for key in degree:
        	if degree[key] == 0:
        		queue.append(degree[key])

        while queue:
        	curr = queue.pop(0)
        	rst.append(curr)
        	for next_course in graph[curr]:
        		degree[next_course] -= 1
        		if degree[next_course] == 0:
        			queue.append(degree[next_course])
        return rst
    
    def build_graph(self, numCourses, degree, prerequisites):
    	graph = [[] for _ in xrange(numCourses)]
    	for i in xrange(len(prerequisites)):
    		course = prerequisites[i][0]
    		dep = prerequisites[i][1]
    		graph[dep] = course
    		degree[course] += 1
    	return graph