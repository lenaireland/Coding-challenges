def reverseParentheses(s):

    s_list = list(s)
    stack = []
    
    removed = 0
    
    for i in range(len(s)):
        if s_list[i-removed] == "(":
            stack.append(i-removed)
            s_list.pop(i-removed)
            removed += 1
        elif s_list[i-removed] == ")":
            start = stack.pop()
            s_list[start:i-removed] = s_list[start:i-removed][::-1]
            s_list.pop(i-removed)
            removed += 1
            
    return "".join(s_list)