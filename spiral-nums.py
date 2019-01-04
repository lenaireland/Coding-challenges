def spiralNumbers(n):

    """Construct a square matrix with a size N × N containing integers from 
    1 to N * N in a spiral order, starting from top-left and in clockwise 
    direction."""

    nums = list(range(n*n, 0, -1))
    
    print(nums)
    
    matrix = []
    
    for r in range(n):
        matrix.append([])
        for c in range(n):
            matrix[r].append(0)
    
    r = 0
    c = 0
    i = 0
    
    while nums:
        while nums and c < n - i:
            matrix[r][c] = nums.pop()
            c += 1
        r += 1
        c -= 1
        while nums and r < n - i:
            matrix[r][c] = nums.pop()
            r += 1
        c -= 1
        r -= 1
        while nums and c >= i:
            matrix[r][c] = nums.pop()
            c -= 1
        r -= 1
        c += 1
        while nums and r >= i + 1:
            matrix[r][c] = nums.pop()
            r -= 1
        c += 1
        r += 1
        i += 1
            
    return matrix

# This is cleaner.  To do: edit my solution above to be more like this.

# def spiralNumbers(n):
#     ans =  [ [0]*n for i in range(n)]
#     p=1;
#     r=0;
#     for i in range(n,0,-2):
#         for a in range(0,i):
#             ans[r][a+r]=p
#             p+=1
#         for b in range(r+1,i+r):
#             ans[b][i-1+r]=p
#             p+=1
#         for c in range(i-2+r,r-1,-1):
#             ans[i-1+r][c]=p
#             p+=1
#         for d in range(i-2+r,r,-1):
#             ans[d][r]=p
#             p+=1
#         r+=1
#     return ans