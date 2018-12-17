def isBeautifulString(inputString):
    """A string is said to be beautiful if b occurs in it no more times than a; 
    c occurs in it no more times than b; etc.

    Given a string, check whether it is beautiful."""
    
    dict = {'a':0,
            'b':0,
            'c':0,
            'd':0,
            'e':0,
            'f':0,
            'g':0,
            'h':0,
            'i':0,
            'j':0,
            'k':0,
            'l':0,
            'm':0,
            'n':0,
            'o':0,
            'p':0,
            'q':0,
            'r':0,
            's':0,
            't':0,
            'u':0,
            'v':0,
            'w':0,
            'x':0,
            'y':0,
            'z':0}

    for char in inputString:
        if char in dict.keys():
            dict[char] += 1
        else:
            dict[char] = 1
            
    print(dict)
    
    count = dict['a']
    
    for key, value in dict.items():
        if value <= count:
            count = value
        else:
            return False
        
    return True