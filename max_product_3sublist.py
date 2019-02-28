class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Given an integer array, find three numbers whose product is maximum and 
        output the maximum product.

        Example 1:
        Input: [1,2,3]
        Output: 6
         
        Example 2:
        Input: [1,2,3,4]
        Output: 24
        """
        
        min1 = 2000
        min2 = 2000
        max1 = -2000
        max2 = -2000
        max3 = -2000
        
        for num in nums:
            if num < min1:
                min2 = min1
                min1 = num
            elif num < min2:
                min2 = num
            
            if num > max1:
                max3 = max2
                max2 = max1
                max1 = num
            elif num > max2:
                max3 = max2
                max2 = num
            elif num > max3:
                max3 = num
                
        if (min1*min2*max1) > (max1*max2*max3):
            return (min1*min2*max1)
        
        return max1*max2*max3