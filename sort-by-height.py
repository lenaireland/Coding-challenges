def sortByHeight(a):
    
    trees = []
    heights = []
    
    for i in range(len(a)):
        if a[i] == -1:
            trees.append(i)
        else:
            heights.append(a[i])
            
    heights.sort(reverse=True)
    
    for n in range(len(a)):
        if a[n] != -1:
            a[n] = heights.pop()
        
    return a