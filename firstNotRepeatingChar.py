def firstNotRepeatingCharacter(s):

    """Given a string s consisting of small English letters, find and return 
    the first instance of a non-repeating character in it. If there is no such 
    character, return '_'."""

    letter_counts = {}
    
    for char in s:
        if char in letter_counts.keys():
            letter_counts[char] += 1
        else:
            letter_counts[char] = 1
            
    for key, value in letter_counts.items():
        if value == 1:
            return key
        
    return '_'