def isCryptSolution(crypt, solution):

    """A cryptarithm is a mathematical puzzle for which the goal is to find the 
    correspondence between letters and digits, such that the given arithmetic 
    equation consisting of letters holds true when the letters are converted to 
    digits.

    You have an array of strings crypt, the cryptarithm, and an an array 
    containing the mapping of letters and digits, solution. The array crypt 
    will contain three non-empty strings that follow the structure: [word1, 
    word2, word3], which should be interpreted as the word1 + word2 = word3 
    cryptarithm.

    If crypt, when it is decoded by replacing all of the letters in the 
    cryptarithm with digits using the mapping in solution, becomes a valid 
    arithmetic equation containing no numbers with leading zeroes, the answer 
    is true. If it does not become a valid arithmetic solution, the answer is 
    false.

    Note that number 0 doesn't contain leading zeroes (while for example 00 or 
    0123 do)."""
        
    nums = ['','','']
    
    for i in range(3):
        for j in range(len(crypt[i])):
            for sets in solution:
                if crypt[i][j] == sets[0]:
                    nums[i] += sets[1]
                    
    num1 = ''.join(nums[0])
    num2 = ''.join(nums[1])
    num3 = ''.join(nums[2])
    
    if len(num1) > 1 and num1[0] == '0':
        return False
    if len(num2) > 1 and num2[0] == '0':
        return False
    if len(num3) > 1 and num3[0] == '0':
         return False
        
    if int(num1) + int(num2) == int(num3):
        return True
    return False