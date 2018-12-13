def extractEachKth(inputArray, k):
    """Given array of integers, remove each kth element from it."""
    
    new_array = []
    
    for i in range(len(inputArray)):
        if (i+1) % k != 0:
            new_array.append(inputArray[i])
            
    return new_array