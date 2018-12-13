def differentSymbolsNaive(s):

    """Given a string, find the number of different characters in it."""

    chars = set()
    
    for char in s:
        chars.add(char)
        
    return len(chars)