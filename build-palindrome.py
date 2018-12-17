def is_palindrome(st):
    
    for i in range(int(len(st)/2)):
        if st[i] != st[-1-i]:
            return False
    return True
        

def buildPalindrome(st):
    """Given a string, find the shortest possible string which can be achieved 
    by adding characters to the end of initial string to make it a palindrome.
    """
    
    if is_palindrome(st):
        return st
    return ''.join([st[0], buildPalindrome(''.join(st[1:])), st[0]]) 