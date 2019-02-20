# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        
        Given a linked list, determine if it has a cycle in it.

        To represent a cycle in the given linked list, we use an integer pos 
        which represents the position (0-indexed) in the linked list where tail 
        connects to. If pos is -1, then there is no cycle in the linked list.
        """
        
        if head is None:
            return False
        
        current = head
        seen = set([current])
        
        while current.next is not None:
            current = current.next
            if current in seen:
                return True
            seen.add(current)
        
        return False