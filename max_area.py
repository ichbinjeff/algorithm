class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        col = len(grid[0])
        max_area = 0
        visited = set()
        for i in xrange(row):
            for j in xrange(col):
                if (i,j) not in visited and grid[i][j] == 1:
                    max_area = max(max_area, self.dfs(grid, visited, i, j))
        return max_area
    
    def dfs(self, grid, visited, i, j):
        if (i,j) in visited or i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
            return 0
        visited.add((i,j))
        return 1 + self.dfs(grid, visited, i+1, j) + self.dfs(grid, visited, i-1, j) + self.dfs(grid, visited, i, j-1) + self.dfs(grid, visited, i, j+1)        