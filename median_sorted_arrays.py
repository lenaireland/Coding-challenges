class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        There are two sorted arrays nums1 and nums2 of size m and n respectively.

        Find the median of the two sorted arrays. The overall run time 
        complexity should be O(log (m+n)).

        You may assume nums1 and nums2 cannot be both empty.

        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        l1 = len(nums1)
        l2 = len(nums2)
        
        # make nums2 longer list
        if l1 > l2:
            nums1, nums2, l1, l2 = nums2, nums1, l2, l1
        if l2 == 0:
            raise ValueError
            
        imin, imax, mid = 0, l1, (l1 + l2 + 1)//2
        # print(imin, imax, mid)
        
        while imin <= imax:
            i = (imin + imax)//2
            j = mid - i
            # print(i,j)
            
            if i < l1 and nums2[j-1] > nums1[i]:
                # i is is too small, increase it
                imin = i + 1
            elif i > 0 and nums1[i-1] > nums2[j]:
                # i is is too big, decrease it
                imax = i - 1
            else:
                # i is perfect
                if i == 0:
                    max_of_left = nums2[j-1]
                elif j == 0:
                    max_of_left = nums1[i-1]
                else:
                    max_of_left = max(nums1[i-1], nums2[j-1])
                
                # print("max left:{}".format(max_of_left))
                # odd number of numbers
                if (l1 + l2) % 2 == 1:
                    return max_of_left
                
                if i == l1:
                    min_of_right = nums2[j]
                elif j == l2:
                    min_of_right = nums1[i]
                else:
                    min_of_right = min(nums1[i], nums2[j])
                
                # print("min right:{}".format(min_of_right))
                return (max_of_left + min_of_right) / 2.0