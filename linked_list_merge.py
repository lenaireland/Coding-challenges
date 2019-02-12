# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: 'ListNode', l2: 'ListNode') -> 'ListNode':
        """Merge two sorted linked lists and return it as a new list. 
        The new list should be made by splicing together the nodes of the first 
        two lists. 
        *in ascending value order"""
        
        if l1 is not None:
            if l2 is None:
                return l1
        elif l2 is not None:
            return l2
        else:
            return None

        new_start = ListNode(None)
        pointer = new_start
        
        while l1 is not None or l2 is not None:
            if l1 is not None and (l2 is None or l1.val < l2.val):
                pointer.next = l1
                l1 = l1.next
            else:
                pointer.next = l2
                l2 = l2.next
            pointer = pointer.next
            
        return new_start.next