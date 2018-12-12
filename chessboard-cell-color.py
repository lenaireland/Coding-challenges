def chessBoardCellColor(cell1, cell2):
    """Given two cells on the standard chess board, determine whether they have 
    the same color or not."""

    return ((ord(cell1[0])+int(cell1[1])) % 2) == ((ord(cell2[0])+int(cell2[1])) % 2)