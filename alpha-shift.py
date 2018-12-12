def alphabeticShift(inputString):
    """Given a string, replace each its character by the next one in the English 
    alphabet (z would be replaced by a)."""
    
    output = []

    for char in inputString:
        if char == 'z':
            output.append('a')
        else:
            output.append(chr(ord(char)+1))
    
    return ''.join(output)