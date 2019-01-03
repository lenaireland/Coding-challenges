def longestWord(text):
    """Define a word as a sequence of consecutive English letters. 
    Find the longest word from the given string."""
    
    words = ''.join((c if c.isalpha() else ' ') for c in text).split()
    
    longest = ''
    
    for word in words:
        if len(word) > len(longest):
            longest = word
            
    return longest