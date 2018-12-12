def variableName(name):
    """Check if the given string is a correct variable name.

    Correct variable names consist only of English letters, digits and 
    underscores and they can't start with a digit."""
    
    if name[0].isdigit():
        return False

    for char in name:
        if char.isalpha():
            continue
        elif char.isdigit():
            continue
        elif char == '_':
            continue
        else:
            return False
    return True