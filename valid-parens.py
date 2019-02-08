class Solution:
    def isValid(self, s: 'str') -> 'bool':
        """Given a string containing just the characters '(', ')', '{', '}', 
        '[' and ']', determine if the input string is valid.

        An input string is valid if:

        Open brackets must be closed by the same type of brackets.
        Open brackets must be closed in the correct order.
        Note that an empty string is also considered valid."""
        
        stack = []
        
        for char in s:
            if char == '(':
                stack.append(char)
            elif char == '{':
                stack.append(char)
            elif char == '[':
                stack.append(char)
            elif char == ')':
                if stack == [] or stack[-1] != '(':
                    return False
                else:
                    stack.pop()
            elif char == '}':
                if stack == [] or stack[-1] != '{':
                    return False
                else:
                    stack.pop() 
            elif char == ']':
                if stack == [] or stack[-1] != '[':
                    return False
                else:
                    stack.pop()
                    
        if stack != []:
            return False
                    
        return True