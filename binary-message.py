def messageFromBinaryCode(code):

    """You are taking part in an Escape Room challenge designed specifically 
    for programmers. In your efforts to find a clue, you've found a binary code 
    written on the wall behind a vase, and realized that it must be an encrypted 
    message. After some thought, your first guess is that each consecutive 8 
    bits of the code stand for the character with the corresponding extended 
    ASCII code.

    Assuming that your hunch is correct, decode the message."""

    code_left = code
    text = []
    
    while code_left:
        bin_letter = code_left[:8]
        code_left = code_left[8:]
        
        int_letter = int(bin_letter, 2)        
        letter = chr(int_letter)       
        text.append(letter)        
        
    return ''.join(text)