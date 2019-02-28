class Solution(object):
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int

        On a N * N grid, we place some 1 * 1 * 1 cubes that are axis-aligned 
        with the x, y, and z axes. Each value v = grid[i][j] represents a tower 
        of v cubes placed on top of grid cell (i, j). Now we view the projection 
        of these cubes onto the xy, yz, and zx planes. A projection is like a 
        shadow, that maps our 3 dimensional figure to a 2 dimensional plane. 
        Here, we are viewing the "shadow" when looking at the cubes from the 
        top, the front, and the side.

        Return the total area of all three projections.

        Example 1:
        Input: [[2]]
        Output: 5

        Example 2:
        Input: [[1,2],[3,4]]
        Output: 17
        """
        
        z = 0
        x = 0
        y = 0
        
        max_y = [0]*len(grid)
        
        for r in range(len(grid)):
            r_max = 0
            for c in range(len(grid[0])):
                if grid[r][c] > 0:
                    z += 1
                    
                if grid[r][c] > r_max:
                    r_max = grid[r][c]
                    
                if grid[r][c] > max_y[c]:
                    max_y[c] = grid[r][c]
                    
            y += r_max
            
        x = sum(max_y)
        
        return x+y+z