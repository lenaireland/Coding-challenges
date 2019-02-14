class Solution:
    def divide(self, dividend: 'int', divisor: 'int') -> 'int':
        """Given two integers dividend and divisor, divide two integers without 
        using multiplication, division and mod operator.

        Return the quotient after dividing dividend by divisor.

        The integer division should truncate toward zero.
        """
        
        if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0):
            sign = 1
        else:
            sign = -1
            
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        result = 0

        while dividend >= divisor:
            i = 1
            temp = divisor
            # loop dividend and temp closer and closer
            while dividend >= temp:
                print(dividend, temp, i, result)
                dividend -= temp
                result += i
                temp <<= 1
                i <<= 1
                print(dividend, temp, i, result)
            # when out of inner while loop, recheck dividend and divisor, 
            # repeat starting again with i = 1 and temp = divisor if dividend 
            # is not greater than divisor
                
        if sign < 0:
            result = -result
            
        return min(max(result, -2**31), 2**31-1)


# Solution TOO SLOW!

# class Solution:
#     def divide(self, dividend: 'int', divisor: 'int') -> 'int':
        
#         result = 0
#         running_sum = 0
        
#         if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0):
#             sign = 1
#         else:
#             sign = -1
            
#         dividend = abs(dividend)
#         divisor = abs(divisor)


#         while running_sum <= (dividend - divisor):
#             result += 1
#             running_sum += divisor
                
#         if sign < 0:
#             result = -result
            
#         return min(max(result, -2147483648),2147483647)