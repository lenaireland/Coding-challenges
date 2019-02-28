# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def mergeTwoLinkedLists(l1, l2):

    """Note: Your solution should have O(l1.length + l2.length) time complexity, 
    since this is what you will be asked to accomplish in an interview.

    Given two singly linked lists sorted in non-decreasing order, your task is 
    to merge them. In other words, return a singly linked list, also sorted in 
    non-decreasing order, that contains the elements from both original lists.
    """
    
    if l1 is None:
        if l2 is None:
            return None
        return l2
    elif l2 is None:
        return l1

    head = ListNode(None)
    current = head
    
    while l1 and l2:
        if l1.value <= l2.value:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    if l1:
        current.next = l1
    elif l2:
        current.next = l2
        
    return head.next