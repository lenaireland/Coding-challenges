class Solution:
    def trap(self, height):
        """
        Given n non-negative integers representing an elevation map where the 
        width of each bar is 1, compute how much water it is able to trap after 
        raining.
        
        :type height: List[int]
        :rtype: int
        """
        
        stack = []
        area = 0
        
        for i in range(len(height)):
            if stack == []:
                if height[i] != 0:
                    stack.append(i)
            elif height[i] < height[stack[-1]]:
                stack.append(i)
            else:
                while stack and height[i] >= height[stack[-1]]:

                    prev = stack.pop()
                    if len(stack) > 0:
                        two_ahead = stack[-1]

                        if height[two_ahead] > height[i]:
                            area += (i-two_ahead-1)*(height[i]-height[prev])
                        else:
                            area += (i-two_ahead-1)*(height[two_ahead]-height[prev])
                stack.append(i)
        
        return area