class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
        Given an unsorted integer array, find the smallest missing positive 
        integer.

        Example 1:
        Input: [1,2,0]
        Output: 3

        Example 2:
        Input: [3,4,-1,1]
        Output: 2

        Example 3:
        Input: [7,8,9,11,12]
        Output: 1
        
        Note: Your algorithm should run in O(n) time and uses constant extra 
        space.
        """
        
        n = len(nums)
        nums_index = [0]*(n+1)
        
        # print(nums_index)
        
        for i in range(n):
            if nums[i] > 0 and nums[i] <= n:
                nums_index[nums[i]] += 1
                
        for index, value in enumerate(nums_index):
            if index == 0:
                continue
            elif value == 0:
                return index
            
        return (n+1 if n > 0 else 1)