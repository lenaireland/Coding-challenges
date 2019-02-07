class Solution:
    def threeSum(self, nums: 'List[int]') -> 'List[List[int]]':
        
        """
        Given an array nums of n integers, are there elements a, b, c in nums 
        such that a + b + c = 0? Find all unique triplets in the array which 
        gives the sum of zero.

        Note:
        The solution set must not contain duplicate triplets.
        """
        
        triples = []
        
        nums.sort()
        # print(nums)
        
        for i in range(len(nums)-2):
            if nums[i] > 0:
                break
            l = i + 1
            r = len(nums)-1
            # print(i, l, r)
            
            while l < r:
                if nums[i] + nums[l] + nums[r] == 0:
                    if ([nums[i], nums[l], nums[r]]) not in triples:
                        triples.append([nums[i], nums[l], nums[r]])
                        # print(triples)
                    l += 1
                    r -= 1
                elif -(nums[i] + nums[l]) > nums[r]:
                    l += 1
                elif -(nums[i] + nums[l]) < nums[r]:
                    r -= 1   
                
                # print(i, l, r)
                    
        return triples