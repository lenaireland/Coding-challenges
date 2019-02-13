# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: 'List[ListNode]') -> 'ListNode':
        """Merge k sorted linked lists and return it as one sorted list. 
        Analyze and describe its complexity.

        Example:

        Input:
        [
          1->4->5,
          1->3->4,
          2->6
        ]
        Output: 1->1->2->3->4->4->5->6
        """
        
        if len(lists) == 0:
            return None

        if len(lists) == 1:
            return lists[0]
        
        if len(lists) == 2:
            
            n1 = lists[0]
            n2 = lists[1]
            
            new_start = ListNode(None)
            pointer = new_start

            while n1 is not None or n2 is not None:
                if n2 is not None and (n1 is None or n2.val < n1.val):
                    pointer.next = n2
                    n2 = n2.next
                else:
                    pointer.next = n1
                    n1 = n1.next
                pointer = pointer.next
            
            return new_start.next
        
        # return self.mergeKLists([self.mergeKLists(lists[1:]),lists[0]])
        
        mid = len(lists)//2
        return self.mergeKLists([self.mergeKLists(lists[mid:]),
                                 self.mergeKLists(lists[:mid])])