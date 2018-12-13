def arrayMaxConsecutiveSum(inputArray, k):
    """Given array of integers, find the maximal possible sum of some of its 
    k consecutive elements.

    Note: tricky b/c need to optimize runtime"""

    max_sum = 0
    
    for i in range(k):
        max_sum += inputArray[i]
        
    new_sum = max_sum
    
    for i in range(len(inputArray)-k):
        
        new_sum = new_sum - inputArray[i] + inputArray[i + k]
        
        if new_sum > max_sum:
            max_sum = new_sum
            
    return max_sum