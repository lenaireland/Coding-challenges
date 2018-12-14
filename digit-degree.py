def digitDegree(n, i=0):
    """Let's define digit degree of some positive integer as the number of times
     we need to replace this number with the sum of its digits until we get to 
     a one digit number.

    Given an integer, find its digit degree."""


    if len(str(n)) == 1:
        return i
    
    next_n = 0
    
    for char in str(n):
        next_n += int(char)
        
    i += 1
    
    return digitDegree(next_n, i)