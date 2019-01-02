def deleteDigit(n):
    """Given some integer, find the maximal number you can obtain by deleting 
    exactly one digit of the given number."""
    
    max_del = 0
    n_list = list(str(n))

    for i in range(len(str(n))):
        
        new_list = n_list[:]
        new_list.pop(i)
        
        i_del = int(''.join(new_list))
        
        if i_del > max_del:
            max_del = i_del
                
    return max_del