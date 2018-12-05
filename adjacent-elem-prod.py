def adjacentElementsProduct(inputArray):
    
    max = inputArray[0]*inputArray[1]

    for i in range(len(inputArray)-1):
        
        num = inputArray[i]*inputArray[i+1]
        
        if num > max:
            max = num
            
    return max