class Solution:
    def isPalindrome(self, x: 'int') -> 'bool':
        
        num = str(x)
        length = len(num)
        
        for i in range(int(length/2)):
            if num[i] != num[length-i-1]:
                return False
            
        return True