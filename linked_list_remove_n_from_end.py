# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: 'ListNode', n: 'int') -> 'ListNode':
        """Given a linked list, remove the n-th node from the end of list and 
        return its head.

        Example:
        Given linked list: 1->2->3->4->5, and n = 2. After removing the second 
        node from the end, the linked list becomes 1->2->3->5."""
        
        i = 1
        current = head
        
        while i < n:
            current = current.next
            i += 1
            
        if current.next is None:
            head = head.next
            return head
        
        current = current.next
        ahead = head
        
        while current.next is not None:
            current = current.next
            ahead = ahead.next

        ahead.next = ahead.next.next    
        
        return head