def returnFailedIndex(sequence):
     
    for n in range(len(sequence)-1):
        if sequence[n+1] - sequence[n] <= 0:
            return n
    return -1


def almostIncreasingSequence(sequence):
    

    index = returnFailedIndex(sequence)
    if index == -1:
        return True
    
    if returnFailedIndex(sequence[:index] + sequence[index+1:]) == -1:
        return True
    if returnFailedIndex(sequence[:index+1] + sequence[index+2:]) == -1:
        return True
    
    return False