def firstDigit(inputString):

    """Find the leftmost digit that occurs in a given string."""

    for char in inputString:
        if char.isdigit():
            return char