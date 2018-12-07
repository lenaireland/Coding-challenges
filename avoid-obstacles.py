def avoidObstacles(inputArray):
    """You are given an array of integers representing coordinates of obstacles 
    situated on a straight line.

    Assume that you are jumping from the point with coordinate 0 to the right. You 
    are allowed only to make jumps of the same length represented by some integer.

    Find the minimal length of the jump enough to avoid all the obstacles."""

    for i in range(2,max(inputArray)):
        modulo_array = [num % i for num in inputArray]
        if 0 not in modulo_array:
            return i
        
    return max(inputArray) + 1