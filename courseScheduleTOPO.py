class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        degree = {}
        graph = self.build_graph(numCourses, degree, prerequisites)
        queue = []
        for key in degree:
            if degree[key] == 0:
                queue.append(key)
    
        while queue:
            top = queue.pop(0)
            prereqs = graph[top]       
            for item in prereqs:
                degree[item] -= 1
                if degree[item] == 0:
                    queue.append(item)
        
        print degree
        for key in degree:
            if degree[key] > 0:
                return False
        return True
            
            
    
    def build_graph(self, numCourses, degree, prerequisites):
        graph = [[] for _ in xrange(numCourses)]
        for i in xrange(numCourses):
            if i not in degree:
                degree[i] = 0
                
        for i in xrange(len(prerequisites)):
            course = prerequisites[i][0]
            prereq = prerequisites[i][1]
            degree[course] += 1
            graph[prereq].append(course)
        return graph