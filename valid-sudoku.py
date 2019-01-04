def sudoku(grid):
    """Sudoku is a number-placement puzzle. The objective is to fill a 9 × 9 
    grid with digits so that each column, each row, and each of the nine 3 × 3 
    sub-grids that compose the grid contains all of the digits from 1 to 9.

    This algorithm should check if the given grid of numbers represents a 
    correct solution to Sudoku."""
    
    valid = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
    nums_check = set()

    for r in range(9):
        for c in range(9):
            nums_check.add(grid[r][c])
        if nums_check != valid:
            return False
        nums_check = set()
    
    for c in range(9):
        for r in range(9):
            nums_check.add(grid[r][c])
        if nums_check != valid:
            return False
        nums_check = set()
        
    for i in range(3):
        for j in range(3):
            print(i)
            print(j)
            nums_check.add(grid[i*3][j*3])
            nums_check.add(grid[i*3+1][j*3])
            nums_check.add(grid[i*3+2][j*3])
            nums_check.add(grid[i*3][j*3+1])
            nums_check.add(grid[i*3+1][j*3+1])
            nums_check.add(grid[i*3+2][j*3+1])
            nums_check.add(grid[i*3][j*3+2])
            nums_check.add(grid[i*3+1][j*3+2])
            nums_check.add(grid[i*3+2][j*3+2])
            
            if nums_check != valid:
                return False
        nums_check = set()
        
    return True