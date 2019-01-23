def reverseInParentheses(inputString):

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