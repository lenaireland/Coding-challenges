def bishopAndPawn(bishop, pawn):
    """Given the positions of a white bishop and a black pawn on the standard 
    chess board, determine whether the bishop can capture the pawn in one move.

    The bishop has no restrictions in distance for each move, but is limited to 
    diagonal movement. Check out the example below to see how it can move:"""

    if ord(bishop[0])+int(bishop[1]) == ord(pawn[0])+int(pawn[1]):
        return True

    if ord(bishop[0])-ord(pawn[0]) == int(bishop[1])-int(pawn[1]):
        return True
        
    return False