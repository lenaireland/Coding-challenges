def palindromeRearranging(inputString):
    """Given a string, find out if its characters can be rearranged to form a palindrome."""
    
    dict = {}
    
    for char in inputString:
        if char in dict.keys():
            dict[char] += 1
        else:
            dict[char] = 1
    
    odd = 0
            
    for key, value in dict.items():
        if value % 2 != 0:
            odd += 1
            if odd > 1:
                return False
            
    return True