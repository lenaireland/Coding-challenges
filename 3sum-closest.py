class Solution:
    def threeSumClosest(self, nums: 'List[int]', target: 'int') -> 'int':
        """Given an array nums of n integers and an integer target, find three 
        integers in nums such that the sum is closest to target. Return the sum 
        of the three integers. You may assume that each input would have exactly
        one solution."""
        
        sum = None
        nums.sort()
        
        for i in range(len(nums)-2):
            l = i + 1
            r = len(nums) - 1
            # print(i,l,r)
            
            if sum is None:
                sum = nums[i] + nums[l] + nums[r]
            
            # print(sum)
            
            while l < r:
                if abs(target - (nums[i] + nums[l] + nums[r])) < abs(target - sum):
                    sum = nums[i] + nums[l] + nums[r]
                    
                if target > nums[i] + nums[l] + nums[r]:
                    l += 1
                elif target < nums[i] + nums[l] + nums[r]:
                    r -= 1
                elif target == nums[i] + nums[l] + nums[r]:
                    return target
                
        return sum