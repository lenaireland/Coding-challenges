class Solution:
    def isMatch(self, s: 'str', p: 'str') -> 'bool':

        """Given an input string (s) and a pattern (p), implement regular 
        expression matching with support for '.' and '*'.

        '.' Matches any single character.
        '*' Matches zero or more of the preceding element.
        The matching should cover the entire input string (not partial).

        Note:

        s could be empty and contains only lowercase letters a-z.
        p could be empty and contains only lowercase letters a-z, and 
        characters like . or *."""
        
        import re
        
        string = re.fullmatch(p,s)
        
        if string:
            return True
        return False