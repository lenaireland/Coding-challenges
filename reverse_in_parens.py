def reverseInParentheses(inputString):
    """Write a function that reverses characters in (possibly nested) 
    parentheses in the input string.

    Input strings will always be well-formed with matching ()s."""

    string_list = []
    
    for char in inputString:
        if char == ")":
            prev = string_list.pop()
            reverse = []
            while prev != "(":
                reverse.append(prev)
                prev = string_list.pop()
            string_list = string_list + reverse
        else:
            string_list.append(char)
    
    return "".join(string_list)