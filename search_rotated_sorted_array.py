class Solution:
    def search(self, nums: 'List[int]', target: 'int') -> 'int':
        """Suppose an array sorted in ascending order is rotated at some pivot 
        unknown to you beforehand.

        (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

        You are given a target value to search. If found in the array return 
        its index, otherwise return -1.

        You may assume no duplicate exists in the array.

        Your algorithm's runtime complexity must be in the order of O(log n).

        Example 1:

        Input: nums = [4,5,6,7,0,1,2], target = 0
        Output: 4
        Example 2:

        Input: nums = [4,5,6,7,0,1,2], target = 3
        Output: -1"""
        
        
        if nums == []:
            return -1
        
        first = 0
        last = len(nums)-1
        mid = len(nums)//2
        
        while last >= first and mid >= first:

            if target == nums[last]:
                return last
            elif target == nums[first]:
                return first
            elif target == nums[mid]:
                return mid

            elif target < nums[mid]:
                if target > nums[first]:
                    mid, last = (mid-first)//2 + first, mid - 1
                elif target < nums[first] and nums[mid] < nums[first]:
                    mid, last = (mid-first)//2 + first, mid - 1
                else:
                    first, mid = mid + 1, (last-mid)//2 + mid + 1

            else:
                if target < nums[last]:
                    first, mid = mid + 1, (last-mid)//2 + mid + 1
                elif target > nums[last] and nums[mid] > nums[first]:
                    first, mid = mid + 1, (last-mid)//2 + mid + 1
                else:
                    mid, last = (mid-first)//2 + first, mid - 1
                    
        return -1