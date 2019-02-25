class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Given an integer array nums, find the contiguous subarray (containing 
        at least one number) which has the largest sum and return its sum.
        """
        
        if nums == []:
            return None
        if len(nums) == 1:
            return nums[0]
        
        if nums[0] > 0:
            running_sum = nums[0]
        else:
            running_sum = 0
        max_sum = nums[0]
        
        for i in range(1,len(nums)):
            if running_sum + nums[i] > max_sum:
                max_sum = running_sum + nums[i]
                
            if running_sum + nums[i] > 0:
                running_sum += nums[i]
            else:
                running_sum = 0
                
        return max_sum