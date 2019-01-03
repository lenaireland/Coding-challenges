def differentSquares(matrix):
    """Given a rectangular matrix containing only digits, calculate the number 
    of different 2 × 2 squares in it."""

    squares = set()
    
    for r in range(len(matrix)-1):
        for c in range(len(matrix[0])-1):
            square = (matrix[r][c], 
                      matrix[r][c+1], 
                      matrix[r+1][c], 
                      matrix[r+1][c+1])
            
            squares.add(square)
            
    return len(squares)