# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        n1 = l1.val
        n2 = l2.val
        
        add = n1 + n2
        rem = 0
        
        if add > 9:
            add = add - 10
            rem += 1
            
        l3 = ListNode(add)
        first = l3
        current = l3
            
        while l1.next is not None and l2.next is not None:
            l1 = l1.next
            l2 = l2.next
            
            n1 = l1.val
            n2 = l2.val
            
            add = n1 + n2 + rem
            rem = 0
            
            if add > 9:
                add = add - 10
                rem += 1
            
            l3 = ListNode(add)
            current.next = l3
            current = l3
            
        while l1.next is None and l2.next is not None:
            l2 = l2.next
            
            n2 = l2.val
            
            add = n2 + rem
            rem = 0
            
            if add > 9:
                add = add - 10
                rem += 1
            
            l3 = ListNode(add)
            current.next = l3
            current = l3
            
        while l1.next is not None and l2.next is None:
            l1 = l1.next
            
            n1 = l1.val
            
            add = n1 + rem
            rem = 0
            
            if add > 9:
                add = add - 10
                rem += 1
            
            l3 = ListNode(add)
            current.next = l3
            current = l3

        if rem > 0:
            l3 = ListNode(rem)
            current.next = l3
            
        return first