class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        
        Given a collection of distinct integers, return all possible permutations.

        Example:
        Input: [1,2,3]
        Output:
        [
          [1,2,3],
          [1,3,2],
          [2,1,3],
          [2,3,1],
          [3,1,2],
          [3,2,1]
        ]
        """
        
        if len(nums) == 0:
            return None
        
        if len(nums) == 1:
            return [[nums[0]]]
        
        perms = []
        
        for i in range(len(nums)):
            recurse = self.permute(nums[0:i] + nums[i+1:len(nums)])
            for item in recurse:
                perms.append(item + [nums[i]])
            
        return perms