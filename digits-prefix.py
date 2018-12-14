def longestDigitsPrefix(inputString):
    """Given a string, output its longest prefix which contains only digits."""
    
    if not inputString[0].isdigit():
        return ''
    
    output = []

    for char in inputString:
        if char.isdigit():
            output.append(char)
        else:
            break
    
    return ''.join(output)