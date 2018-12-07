def arrayChange(inputArray):
    """You are given an array of integers. On each move you are allowed 
    to increase exactly one of its element by one. Find the minimal number of 
    moves required to obtain a strictly increasing sequence from the input."""
    
    inc = 0

    for i in range(len(inputArray)-1):
        if inputArray[i+1] <= inputArray[i]:
            inc += inputArray[i] - inputArray[i+1] + 1
            inputArray[i+1] = inputArray[i] + 1
            
    return inc