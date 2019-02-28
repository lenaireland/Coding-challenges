class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int

        Given a 2d grid map of '1's (land) and '0's (water), count the number of 
        islands. An island is surrounded by water and is formed by connecting 
        adjacent lands horizontally or vertically. You may assume all four edges 
        of the grid are all surrounded by water.

        Example 1:
        Input:
        11110
        11010
        11000
        00000
        Output: 1

        Example 2:
        Input:
        11000
        11000
        00100
        00011
        Output: 3
        """
        
        islands = 0
        
        if grid == []:
            return islands
        
        
        n_rows = len(grid)
        n_cols = len(grid[0])
        
        for r in range(n_rows):
            for c in range(n_cols):
                if grid[r][c] == "1":
                    stack = [[r,c]]
                    grid[r][c] = 0
                    islands += 1
                    
                    while stack:
                        x,y = stack.pop()
                        if (x-1) >= 0 and grid[x-1][y] == "1":
                            stack.append([x-1, y])
                            grid[x-1][y] = 0
                        if (x+1) < n_rows and grid[x+1][y] == "1":
                            stack.append([x+1, y])
                            grid[x+1][y] = 0
                        if (y-1) >= 0 and grid[x][y-1] == "1":
                            stack.append([x, y-1])
                            grid[x][y-1] = 0
                        if (y+1) < n_cols and grid[x][y+1] == "1":
                            stack.append([x, y+1])
                            grid[x][y+1] = 0
        
        return islands