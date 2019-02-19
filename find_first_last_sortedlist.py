class Solution:
    def searchRange(self, nums: 'List[int]', target: 'int') -> 'List[int]':

        """Given an array of integers nums sorted in ascending order, find the 
        starting and ending position of a given target value.

        Your algorithm's runtime complexity must be in the order of O(log n).

        If the target is not found in the array, return [-1, -1]."""
        
        start = 0
        mid = len(nums)//2
        end = len(nums) - 1
        
        if nums == []:
            return [-1,-1]
        
        if target < nums[start]:
            return [-1,-1]
        
        if target > nums[end]:
            return [-1,-1]
        
        if nums[start] == target:
            n1 = start
        else:
            while start < end:
                print(start, mid, end)

                if target <= nums[mid]:
                    end = mid
                    mid = (mid-start)//2 + start

                elif target > nums[mid]:
                    start = mid + 1
                    mid = (end-mid)//2 + mid
                
                if nums[start] == target:
                    n1 = start
                    print(n1)
                    break
                
        try:
            if n1:
                pass
        except:
            return [-1,-1]
                
                
        mid = len(nums)//2
        end = len(nums) - 1
        
        if nums[end] == target:
            n2 = end
        else:
            while start < end:
                print(start, mid, end)

                if target < nums[mid]:
                    end = mid - 1
                    mid = (mid-start)//2 + start

                elif target >= nums[mid]:
                    start = mid
                    mid = (end-mid)//2 + mid + 1
                
                if nums[end] == target:
                    n2 = end
                    break
                    
        try:
            return [n1,n2]
        except:
            return [-1,-1]