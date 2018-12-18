def lineEncoding(s):
    """Given a string, return its encoding defined as follows:

    First, the string is divided into the least possible number of disjoint 
    substrings consisting of identical characters for example, "aabbbc" is 
    divided into ["aa", "bbb", "c"]. Next, each substring with length greater 
    than one is replaced with a concatenation of its length and the repeating 
    character for example, substring "bbb" is replaced by "3b". Finally, all 
    the new strings are concatenated together in the same order and a new 
    string is returned."""
    
    prev = None
    count = 0
    new_s = ''

    for char in s:
        if prev == None:
            prev = char
            count = 1
        elif char == prev:
            count += 1
        else:
            if count > 1:
                new_s = ''.join([new_s, str(count), prev])
            else:
                new_s = ''.join([new_s, prev])
            prev = char
            count = 1
            
    if count > 1:
        return ''.join([new_s, str(count), prev])
    
    return ''.join([new_s, prev])