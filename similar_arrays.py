def areSimilar(a, b):
    """Two arrays are called similar if one can be obtained from another by 
    swapping at most one pair of elements in one of the arrays.

    Given two arrays a and b, check whether they are similar."""

#     if a == b:
#         return True    
    
#     for i in range(len(a)):
#         for j in range(len(a)):
#             copy_a = a[:]
#             copy_a[i], copy_a[j] = copy_a[j], copy_a[i]
#             if copy_a == b:
#                 return True
    
#     return False
#     
    if a == b:
        return True
    
    diff_indices = []
    
    for i in range(len(a)):
        if a[i] != b[i]:
            diff_indices.append(i)
            
    if (len(diff_indices) ==2 and 
        a[diff_indices[0]] == b[diff_indices[1]] and 
        a[diff_indices[1]] == b[diff_indices[0]]):
        return True
    
    return False