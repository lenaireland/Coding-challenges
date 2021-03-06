class Solution:
    def maxArea(self, height):
        """

        Given n non-negative integers a1, a2, ..., an , where each represents a 
        point at coordinate (i, ai). n vertical lines are drawn such that the 
        two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which 
        together with x-axis forms a container, such that the container contains
        the most water.

        Note: You may not slant the container and n is at least 2.

        :type height: List[int]
        :rtype: int
        """   
        
        left = 0
        right = len(height)-1
        area = 0
        
        while left != right:
            
            new_area = min(height[left],height[right])*(right-left)
            
            if new_area > area:
                area = new_area
                
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
                
        return area