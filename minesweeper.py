def minesweeper(matrix):
    """In the popular Minesweeper game you have a board with some mines and 
    those cells that don't contain a mine have a number in it that indicates 
    the total number of mines in the neighboring cells. Starting off with some 
    arrangement of mines we want to create a Minesweeper game setup."""
    
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    
    adj_mines = []
    
    adj_row = [0]*num_cols
    
    for i in range(num_rows):
        adj_mines.append(adj_row[:])
        
    for r in range(num_rows):
        for c in range(num_cols):
            if matrix[r][c] == True:
                if (r-1) in range(num_rows) and (c-1) in range(num_cols):
                    adj_mines[r-1][c-1] += 1
                if (r-1) in range(num_rows) and (c) in range(num_cols):
                    adj_mines[r-1][c] += 1
                if (r-1) in range(num_rows) and (c+1) in range(num_cols): 
                    adj_mines[r-1][c+1] += 1
                if (r) in range(num_rows) and (c-1) in range(num_cols):
                    adj_mines[r][c-1] += 1
                if (r) in range(num_rows) and (c+1) in range(num_cols): 
                    adj_mines[r][c+1] += 1
                if (r+1) in range(num_rows) and (c-1) in range(num_cols):
                    adj_mines[r+1][c-1] += 1
                if (r+1) in range(num_rows) and (c) in range(num_cols):
                    adj_mines[r+1][c] += 1
                if (r+1) in range(num_rows) and (c+1) in range(num_cols): 
                    adj_mines[r+1][c+1] += 1

    
    return adj_mines