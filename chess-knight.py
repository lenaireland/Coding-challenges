def chessKnight(cell):
    """Given a position of a knight on the standard chessboard, find the number 
    of different moves the knight can perform.

    The knight can move to a square that is two squares horizontally and one 
    square vertically, or two squares vertically and one square horizontally 
    away from it. The complete move therefore looks like the letter L. Check 
    out the image below to see all valid moves for a knight piece that is 
    placed on one of the central squares"""
    
    alpha = ord(cell[0].lower())
    num = int(cell[1])
    
    possible = 0
    
    if alpha - 2 > 96 and alpha - 2 < 105 and num + 1 > 0 and num + 1 < 9:
        possible += 1
        
    if alpha - 2 > 96 and alpha - 2 < 105 and num - 1 > 0 and num - 1 < 9:
        possible += 1
        
    if alpha - 1 > 96 and alpha - 1 < 105 and num + 2 > 0 and num + 2 < 9:
        possible += 1
        
    if alpha - 1 > 96 and alpha - 1 < 105 and num - 2 > 0 and num - 2 < 9:
        possible += 1
        
    if alpha + 1 > 96 and alpha + 1 < 105 and num + 2 > 0 and num + 2 < 9:
        possible += 1
        
    if alpha + 1 > 96 and alpha + 1 < 105 and num - 2 > 0 and num  - 2 < 9:
        possible += 1
        
    if alpha + 2  > 96 and alpha + 2 < 105 and num + 1 > 0 and num + 1 < 9:
        possible += 1
        
    if alpha + 2 > 96 and alpha + 2 < 105 and num - 1 > 0 and num - 1 < 9:
        possible += 1
        
    return possible