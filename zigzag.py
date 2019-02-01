class Solution:
    def convert(self, s, numRows):
        """
        The string "PAYPALISHIRING" is written in a zigzag pattern on a given 
        number of rows like this: (you may want to display this pattern in a 
        fixed font for better legibility)
        P   A   H   N
        A P L S I I G
        Y   I   R
        And then read line by line: "PAHNAPLSIIGYIR"

        Write the code that will take a string and make this conversion given a 
        number of rows.

        :type s: str
        :type numRows: int
        :rtype: str
        """
        
        if numRows == 1:
            return s
        
        matrix = []
        for i in range(numRows):

            # Change from storing matrices of letter to strings
            # matrix.append([])
            matrix.append('')

        r = 0
        
        for i in range(len(s)):
            # print("r:{}".format(r))
            # print("i:{}".format(i))

            # Change from storing matrices of letter to strings
            # matrix[r].append(s[i])
            matrix[r]+=s[i]

            if i % ((numRows-1)*2) < (numRows-1): 
                r += 1
            else:
                r -= 1
                
        # print(matrix)

        # Now don't have to join individual strings first
        # for j in range(len(matrix)):
        #     matrix[j]=''.join(matrix[j])
            
        return ''.join(matrix)