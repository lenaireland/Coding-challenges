class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
        if matrix == []:
            return []
        
        r_min = 0
        r_max = len(matrix) - 1
        c_min = 0
        c_max = len(matrix[0]) - 1
        
        r = 0
        c = 0
        
        out = []
        
        while r_min <= r_max and c_min <= c_max:
            
            # while c <= c_max:
            #     out.append(matrix[r][c])
            #     c += 1
            # c -= 1
            # r += 1
            # r_min += 1                
            # while r <= r_max:
            #     out.append(matrix[r][c])
            #     r += 1
            # r -= 1
            # c -= 1
            # c_max -= 1
            #
            # if r_min <= r_max:
            #     while c >= c_min:
            #         out.append(matrix[r][c])
            #         c -= 1
            #     c += 1
            #     r -= 1
            #     r_max -= 1
            # if c_min <= c_max:
            #     while r >= r_min:
            #         out.append(matrix[r][c])
            #         r -= 1
            #     r += 1
            #     c += 1
            #     c_min += 1

            for c in range(c_min, c_max+1):
                out.append(matrix[r][c])
            r_min += 1

            for r in range(r_min, r_max+1):
                out.append(matrix[r][c])
            c_max -= 1

            if r_min <= r_max:
                for c in range(c_max, c_min-1,-1):
                    out.append(matrix[r][c])
                r_max -= 1

            if c_min <= c_max:
                for r in range(r_max, r_min-1,-1):
                    out.append(matrix[r][c])
                c_min += 1
            
        return out