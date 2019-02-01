class Solution:
    def reverse(self, x):
        """
        Given a 32-bit signed integer, reverse digits of an integer.
        Assume we are dealing with an environment which could only store 
        integers within the 32-bit signed integer range: [−231,  231 − 1]. 
        For the purpose of this problem, assume that your function returns 0 
        when the reversed integer overflows.

        :type x: int
        :rtype: int
        """
        sign = ''
        
        if x < 0:
            sign = '-'
        
        new_num = []
        for char in str(x):
            if char != '-':
                new_num.insert(0,char)
            
        new_num.insert(0,sign)
        
        num = int(''.join(new_num))
        
        if num > 2**31 - 1:
            return 0
        
        if num < -2**31:
            return 0
        
        return num