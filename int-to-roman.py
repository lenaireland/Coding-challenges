class Solution:
    def intToRoman(self, num: 'int') -> 'str':
        """Given an integer, convert it to a roman numeral. 
        Input is guaranteed to be within the range from 1 to 3999."""
        
        thousand = num // 1000
        hundred = (num - thousand*1000) // 100
        ten = (num - thousand*1000 - hundred*100) // 10
        one = (num - thousand*1000 - hundred*100 - ten*10)
               
        string = ''
               
        if thousand:
               string += 'M'*thousand
                
        if hundred:
            if hundred < 4:
                string += 'C'*hundred
            elif hundred == 4:
                string += 'CD'
            elif hundred > 4 and hundred < 9:
                string += 'D' + 'C'*(hundred-5)
            elif hundred == 9:
                string += 'CM'
                
        if ten:
            if ten < 4:
                string += 'X'*ten
            elif ten == 4:
                string += 'XL'
            elif ten > 4 and ten < 9:
                string += 'L' + 'X'*(ten-5)
            elif ten == 9:
                string += 'XC'
        
        if one:
            if one < 4:
                string += 'I'*one
            elif one == 4:
                string += 'IV'
            elif one > 4 and one < 9:
                string += 'V' + 'I'*(one-5)
            elif one == 9:
                string += 'IX'
               
        return string